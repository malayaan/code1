import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from sklearn.model_selection import KFold, train_test_split
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.metrics import make_scorer
from sklearn.ensemble import IsolationForest
from sklearn.datasets import load_iris
from threading import Thread
import time

class AnomalyDetector:
    def __init__(self, estimator, X_train, X_test, y_train, y_test, scorer):
        self.estimator = estimator
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = make_scorer(scorer, greater_is_better=True)
        self.scores = []
        self.last_time = None  # Store last time here
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Optimization Progress")
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)

    def update_plot(self):
        if len(self.scores) == 1:
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.ax.clear()
        self.ax.plot(self.scores, 'r.-')
        self.ax.set_title('Dynamic Plot of Minimum Scores')
        self.ax.set_xlabel('Iteration')
        self.ax.set_ylabel('Score')
        self.fig.canvas.draw()

    def run_optimization(self, search_space, n_iter=50, cv_splits=3):
        kf = KFold(n_splits=cv_splits, shuffle=True, random_state=42)
        # Adjust max_samples based on the size of X_train
        max_samples = min(200, len(self.X_train))  # Ensure max_samples does not exceed number of samples
        search_space['max_samples'] = Integer(50, max_samples)
        optimizer = BayesSearchCV(
            estimator=self.estimator,
            search_spaces=search_space,
            n_iter=n_iter,
            scoring=self.scorer,
            cv=kf,
            random_state=42,
            n_jobs=-1
        )
        optimizer.fit(self.X_train, self.y_train, callback=self.optimization_callback)
        best_model = optimizer.best_estimator_
        best_model.fit(self.X_train)
        y_pred_test = best_model.predict(self.X_test)
        test_score = self.scorer(best_model, self.X_test, self.y_test)
        self.save_results(optimizer)
        return optimizer.best_params_, test_score

    def optimization_callback(self, res):
        current_time = time.time()
        duration = current_time - (self.last_time if self.last_time is not None else current_time)
        self.last_time = current_time
        self.scores.append(np.min(res.func_vals))
        self.update_plot()
        with open('performance.txt', 'a') as f:
            f.write(f"Iteration No: {len(res.func_vals)}, "
                    f"Time taken: {duration:.4f}, "
                    f"Function value obtained: {res.func_vals[-1]:.4f}, "
                    f"Current minimum: {np.min(res.func_vals):.4f}\n")

    def save_results(self, optimizer):
        with open('final_results.txt', 'w') as f:
            f.write(f"Best Parameters: {optimizer.best_params_}\n")
            f.write(f"Best Score: {optimizer.best_score_}\n")

    def start(self):
        thread = Thread(target=self.run_optimization, args=({
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),  # This will get adjusted in run_optimization
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        },))
        thread.start()
        self.root.mainloop()

def prepare_data():
    iris = load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0).astype(int)
    return train_test_split(X, y, test_size=0.3, random_state=42)

def custom_scorer_function(y_true, y_pred):
    return -np.mean(y_true != y_pred)

def main():
    X_train, X_test, y_train, y_test = prepare_data()
    print("X_train shape:", X_train.shape)
    print("y_train shape:", y_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_test shape:", y_test.shape)

    detector = AnomalyDetector(
        estimator=IsolationForest(random_state=42),
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        scorer=custom_scorer_function
    )
    detector.start()

if __name__ == "__main__":
    main()
