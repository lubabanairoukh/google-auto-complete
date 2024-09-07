from dataclasses import dataclass

@dataclass
class AutoCompleteData:
    completed_sentence: str  # The sentence that was matched or completed
    source_text: str          # The name or path of the file where the sentence was found
    offset: int              # The line number or position within the source text where the sentence is located
    score: int                # The score assigned to the matched sentence, indicating its relevance
