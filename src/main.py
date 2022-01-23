from transformers import AutoModel, AutoTokenizer
from src.utils.helpers import json_parser


class BenFeroGenerator:
    def __init__(self, ben_fero_json_path: str, others_json_path: str):
        """
        Provides functionality for training and inferring on a generator which generates lines in the style of literary
        genius Ben Fero, trained in an adversarial fashion with a Turkish BERT (BERTurk) discriminator.
        @param ben_fero_json_path: path to the JSON file containing Ben Fero lyrics
        @param others_json_path: path to the JSON file containing lyrics from other lower-tier rappers
        """
        self.tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
        self.discriminator = AutoModel.from_pretrained("dbmdz/bert-base-turkish-cased")
        self.generator = None
        self.ben_fero_lyrics = json_parser(ben_fero_json_path)
        self.other_lyrics = json_parser(others_json_path)

    def train(self):
        """
        Trains `self.generator` and `self.discriminator` in an adversarial fashion. `self.generator` tries to trick
        `self.discriminator` into thinking that the lines it generates belong to a Ben Fero song. `self.discriminator`
        tries to avoid that and correctly classify any given line.
        """
        pass

    def __call__(self, starting_line: str) -> str:
        """
        Generates a new line in the style of Ben Fero, rhyming with a starting line. We don't need to be coherent across
        multiple lines since the great poet Ben Fero himself is not, conditioning on a single line should be enough.
        @param starting_line: starting line
        @return: a line in the style of Ben Fero rhyming with `starting_line`
        """
        return starting_line
