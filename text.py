from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """Russian foreign minister Sergei Lavrov said that creating a Palestinian state was the "most reliable" solution for peace in Israel as fighting terrorism alone would not ensure security. Speaking at a press conference with the head of the Arab League, Ahmed Aboul Gheit, who visited Russia after Hamas launched a massive surprise attack, Sergei Lavrov said that creating a “Palestinian state that would live side by side with Israel... is the most reliable path to solve (the conflict).”

Israel-Palestine Latest: Israeli soldiers stand guard near damage caused by a rocket after if was fired from the Gaza Strip towards Israel.(Reuters)
Israel-Palestine Latest: Israeli soldiers stand guard near damage caused by a rocket after if was fired from the Gaza Strip towards Israel.(Reuters)
“We cannot agree with those who say that security can only be ensured through a fight with terrorism,” he said, adding that Moscow was "deeply concerned that hundreds of Israelis and Palestinians have died and that the Gaza Sector has been declared a target for Israeli retaliation."
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
