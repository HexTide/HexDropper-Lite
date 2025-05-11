from hexlib.ai_prompt import PromptBuilder
from hexroot.base import BaseBot
from hexlib.config import TEMPLATE_DIR
from dropper.config import AFFILIATE_LINK, TEMPLATE_FILE, TEMPLATE_DIR
import os

class Bot(BaseBot):
    def __init__(self):
        super().__init__(name="HexDropper-Lite")

    def start(self):
        prompt = PromptBuilder(template_dir=TEMPLATE_DIR)
        prompt_path = os.path.join(TEMPLATE_DIR, TEMPLATE_FILE)
        prompt.load_template(prompt_path)
        msg = prompt.render(user="Aytuğ", link=AFFILIATE_LINK)
        print(f"[{self.name}] Generated message:\n{msg}")
