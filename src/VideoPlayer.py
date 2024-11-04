import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class VideoPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Local Search Video Player")
        self.root.geometry("1000x1000")

        self.ax = None

        self.states = []
        self.previous_action = []
        self.values = []
        self.angles = None
        self.index = 0
        self.is_playing = False
        self.speed = 1.0
        self.orientation = "Interactive"

    def setup_ui(self):
        self.setup_ui()

    def play_button_handler(self):
        self.is_playing = not self.is_playing
        self.play_button.config(text="Pause" if self.is_playing else "Play")
        if self.is_playing:
            self.play_matrices()

    def play_matrices(self):
        while self.is_playing and self.index < len(self.states):
            self.display_state(self.states[self.index])
            self.index += 1
            self.progress_value.set((self.index / len(self.states)) * 100)
            self.root.update()
            time.sleep(1 / self.speed)

    def seek(self, value):
        self.index = int(float(value) / 100 * len(self.states))
        if self.index < len(self.states):
            self.display_state(self.states[self.index])

    def speed_scale_handler(self, value):
        self.speed = float(value)

    def load_handler(self):
        file_path = filedialog.askopenfilename(title="Select Experiment File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            self.load_states(file_path)

    def load_states(self, file_path):
        try:
            with open(file_path, 'r') as f:
                data = f.readlines()

            states = []
            previous_action = []
            values = []
            current_state = []
            current_frame = []

            for line in data:
                stripped_line = line.strip()
                if stripped_line.startswith("Iteration"):
                    arr = stripped_line.split(':')
                    values.append(int(arr[1]))

                    if arr[2] != 'None':
                        previous_action.append([list(map(int, arr[2].split('-'))), list(map(int, arr[3].split('-')))])

                    if current_state:
                        states.append(current_state)
                        current_state = []
                    continue

                if stripped_line:
                    row = list(map(float, stripped_line.split()))
                    current_frame.append(row)
                else:
                    if current_frame:
                        current_state.append(np.array(current_frame))
                        current_frame = []

            if current_frame:
                current_state.append(np.array(current_frame))

            if current_state:
                states.append(current_state)

            self.states = states
            self.previous_action = previous_action
            self.values = values
            self.index = 0
            self.progress_value.set(0)

            if states:
                self.display_state(states[0])

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def update_orientation(self):
        if self.angles is not None:
            self.ax.view_init(elev=self.angles[0], azim=self.angles[1], roll=self.angles[2])

            self.canvas.draw()

    def display_state(self, states):
        if self.index > len(self.states) - 1:
            if self.index == len(self.states):
                self.play_button_handler()

            pass

        self.ax.cla()

        if self.angles is not None:
            self.ax.view_init(elev=self.angles[0], azim=self.angles[1], roll=self.angles[2])

        self.ax.set_box_aspect([1, 1, 1])

        for z in range(len(states)):
            matrix = states[z]
            rows, cols = matrix.shape

            x = np.arange(cols)
            y = np.arange(rows)
            x, y = np.meshgrid(x, y)

            for i in range(rows):
                for j in range(cols):
                    value = matrix[i, j]
                    pad_color = 'yellow' if (
                            self.index < len(self.previous_action) and
                            ([z, i, j] == self.previous_action[self.index][0] or [z, i, j] == self.previous_action[self.index][1])
                                             ) else 'white'
                    self.ax.text(j, i, z,
                                 f'{value:.1f}', color='black',
                                 fontsize=8, ha='center', va='center',
                                 bbox=dict(facecolor=pad_color, edgecolor='none', boxstyle='round,pad=0.1'))

            for i in range(rows):
                for j in range(cols - 1):
                    self.ax.plot([j, j + 1], [i, i], [z, z], color='blue', alpha=0.5)

            if z < len(states) - 1:
                for i in range(rows):
                    for j in range(cols):
                        self.ax.plot([j, j], [i, i], [z, z + 1], color='blue', alpha=0.5)

            for i in range(rows - 1):
                for j in range(cols):
                    self.ax.plot([j, j], [i, i + 1], [z, z], color='blue', alpha=0.5)

        self.ax.set_title(f"Objective value: {self.values[self.index]}", pad=20)

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        self.canvas.draw()

    def update_view_label_handler(self):
        self.view_label.config(text=f"{self.orientation}")
        self.update_orientation()

    def setup_ui(self):
        control_frame = tk.Frame(self.root, bg="#e0e0eb")
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.play_button = tk.Button(control_frame, text="Play", command=self.play_button_handler, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(control_frame, text="Load Experiment File", command=self.load_handler, bg="#5bc0de", fg="white", font=("Arial", 10, "bold"))
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.progress_value = tk.DoubleVar()
        self.progress_bar = tk.Scale(control_frame, variable=self.progress_value, from_=0, to=100, orient='horizontal',
                                     length=400, command=self.seek, bg="#dcdcdc")
        self.progress_bar.pack(side=tk.LEFT, padx=5)

        speed_frame = tk.Frame(self.root, bg="#f0f0f5")
        speed_frame.pack(side=tk.TOP, pady=10)

        self.speed_label = tk.Label(speed_frame, text="Playback Speed:", bg="#f0f0f5", font=("Arial", 10))
        self.speed_label.pack(side=tk.LEFT)

        self.speed_scale = tk.Scale(speed_frame, from_=0.5, to=3.0, resolution=0.1, orient='horizontal',
                                    command=self.speed_scale_handler, bg="#dcdcdc")
        self.speed_scale.set(self.speed)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        orientation_frame = tk.Frame(self.root, bg="#f0f0f5")
        orientation_frame.pack(side=tk.TOP, pady=10)

        self.view_label = tk.Label(orientation_frame, text=f"{self.orientation}", bg="#f0f0f5", font=("Arial", 10, "bold"))
        self.view_label.pack(side=tk.LEFT)

        view_frame = tk.Frame(self.root, bg="#f0f0f5")
        view_frame.pack(side=tk.TOP, pady=10)

        self.interactive_button = tk.Button(view_frame, text=f"Interactive", command=lambda: (setattr(self, 'angles', None), setattr(self, 'orientation', 'Interactive'), self.update_view_label_handler()),
                                           bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.interactive_button.pack(side=tk.LEFT, padx=2)

        self.front_view_button = tk.Button(view_frame, text=f"Front", command=lambda: (setattr(self, 'angles', [90, -90, 0]), setattr(self, 'orientation', "Front"), self.update_view_label_handler()),
                           bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.front_view_button.pack(side=tk.LEFT, padx=2)

        self.back_view_button = tk.Button(view_frame, text=f"Back", command=lambda: (setattr(self, 'angles', [0, 180, 0]), setattr(self, 'orientation', "Back"), self.update_view_label_handler()),
                                           bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.back_view_button.pack(side=tk.LEFT, padx=2)

        self.left_view_button = tk.Button(view_frame, text=f"Left", command=lambda: (setattr(self, 'angles', [0, -90, 0]), setattr(self, 'orientation', "Left"), self.update_view_label_handler()),
                                           bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.left_view_button.pack(side=tk.LEFT, padx=2)

        self.right_view_button = tk.Button(view_frame, text=f"Right", command=lambda: (setattr(self, 'angles', [0, 90, 0]), setattr(self, 'orientation', "Right"), self.update_view_label_handler()),
                                          bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.right_view_button.pack(side=tk.LEFT, padx=2)

        self.top_view_button = tk.Button(view_frame, text=f"Top", command=lambda: (setattr(self, 'angles', [-90, 90, 0]), setattr(self, 'orientation', "Top"), self.update_view_label_handler()),
                                          bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.top_view_button.pack(side=tk.LEFT, padx=2)

        self.bottom_view_button = tk.Button(view_frame, text=f"Bottom", command=lambda: (setattr(self, 'angles', [0, 0, 0]), setattr(self, 'orientation', "Bottom"), self.update_view_label_handler()),
                                           bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
        self.bottom_view_button.pack(side=tk.LEFT, padx=2)

        fig_frame = tk.Frame(self.root, bg="#f0f0f5")
        fig_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.figure = plt.Figure(figsize=(6, 6), dpi=100)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.figure, master=fig_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, fig_frame)
        toolbar.update()
        toolbar.pack(side=tk.TOP, fill=tk.X)
