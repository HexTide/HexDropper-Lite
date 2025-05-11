from hexlib.ai_prompt import PromptBuilder
from hexlib.config import TEMPLATE_DIR
from dropper.config import AFFILIATE_LINK, TEMPLATE_FILE

def generate_message(username: str):
    prompt = PromptBuilder(template_dir=TEMPLATE_DIR)
    prompt.load_template(TEMPLATE_FILE)
    return prompt.render(user=username, link=AFFILIATE_LINK)
