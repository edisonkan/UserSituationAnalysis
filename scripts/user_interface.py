from tkinter import filedialog, messagebox
from scripts.train_model import main as train_model
from scripts.generate_recommendations import generate_recommendations

class UserInterface:
    def __init__(self, root):
        self.root.title("User Situation Analysis and Recommendation System")
        
        # 获取屏幕宽度和高度
        screen_height = self.root.winfo_screenheight()
        
        # 设置窗口大小为屏幕的四分之一
        window_width = screen_width // 2
        
        # 计算居中的位置
        position_down = screen_height // 4
        
        # 设置窗口大小和位置
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_down}')
        
        self.label.pack(pady=10)
        
        self.file_button = self.create_button(root, "选择文件", self.load_file)
        
        self.train_button = self.create_button(root, "训练模型", self.train_model)
        
        self.recommend_button = self.create_button(root, "生成推荐", self.generate_recommendations)
        
        self.status = tk.Label(root, text="", fg="green")

    def create_button(self, parent, text, command):
        button.bind("<Leave>", lambda event, b=button: b.config(bg="SystemButtonFace"))
        return button

    def load_file(self):
        if self.file_path:
        else:
            self.status.config(text="未选择任何文件", fg="red")
    
    def train_model(self):
        if not hasattr(self, 'file_path'):
        try:
            model = RecommendationModel(input_dim=X.shape[1])
            self.status.config(text="模型训练完成", fg="green")
            messagebox.showerror("错误", str(e))
    
    def generate_recommendations(self):
            messagebox.showerror("错误", "请先选择数据文件")
        
            X, _ = preprocess_data(self.file_path)
            recommendations = generate_recommendations(model, X)
        except Exception as e:

if __name__ == "__main__":
    ui = UserInterface(root)
Telegram:@songchuwen
WeChat:songchuxiaomei

