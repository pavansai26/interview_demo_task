import logging
import spacy

# Load the spaCy English small model for entity recognition
logging.info("Loading spaCy English small model...")
nlp = spacy.load("en_core_web_sm")

# Define function to extract entities from text
def extract_entities(text):
    """
    Extracts named entities from a given text using spaCy.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary mapping entity labels to their corresponding text.
    """
    logging.debug(f"Processing text: {text}")
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        logging.debug(f"Found entity: {ent.text} (label: {ent.label_})")
        entities[ent.label_] = ent.text
    return entities