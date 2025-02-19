#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# File name: translate.py
# Author: INV 2578
# Date created: 2024-11-11
# Version = "1.0"
# License =  "CC0 1.0"
# =============================================================================
""" This script is used to automate DeepL translations using Selenium."""
# =============================================================================


# Imports
import re
import time
from typing import Generator
from typing import List
from collections import deque
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webelement import WebElement


# Parameters
FIREFOX_PATH = "/usr/bin/firefox"
GECKODRIVER_PATH = "/opt/geckodriver"
HEADLESS = True

SOURCE_LANG = "en"
OUTPUT_LANG = "fr"
LINK = "https://www.deepl.com/en/translator#" + \
    SOURCE_LANG + "/" + OUTPUT_LANG + "/-"

CHAR_LIMIT = 1500
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

TIMEOUT = 8
SLEEP_TIME = 12.00

# CSS selectors -might break on website updates
INPUT_AREA = "d-textarea[name='source'] div[role='textbox']"
OUTPUT_AREA = "d-textarea[name='target'] div[role='textbox']"

PRINT_DETAILS = False


# ---------------------------------------------------------------------------
# Functions
def initialize_browser() -> webdriver.Remote:
    """
    Initializes a new Firefox browser instance.

    Returns:
        webdriver: A new Firefox browser instance.
    """
    driver_service = Service(GECKODRIVER_PATH, log_output="geckodriver.log")
    options = webdriver.FirefoxOptions()
    options.binary_location = FIREFOX_PATH
    if HEADLESS:
        options.add_argument("-headless")
    return webdriver.Firefox(service=driver_service, options=options)


def load_input_file(file_name: str) -> str:
    """
    Loads the contents of a file into a string.

    Args:
        file_name (str): The name of the file to load.

    Returns:
        str: The contents of the file.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {file_name} not found. Please check, and try again.")
        raise


def split_text_into_sentences(text: str) -> list:
    """
    Splits a block of text into individual sentences.

    Args:
        text (str): The text to split.

    Returns:
        list: A list of sentences.
    """
    return re.split(r"(?<=[\.?!])", text)


def generate_chunks(text: list, char_limit: int = CHAR_LIMIT) -> Generator[str, None, None]:
    """
    Splits a block of text into chunks of a maximum size.

    Args:
        text (list): A list of sentences to split.
        char_limit (int): The maximum size of each chunk.

    Yields:
        str: A chunk of text.
    """
    chunk = deque()
    chunk_length = 0

    for sentence in text:
        sentence_length = len(sentence) + 1  # Add 1 for the space character
        if chunk_length + sentence_length > char_limit:
            yield " ".join(chunk)
            chunk.clear()
            chunk.append(sentence)
            chunk_length = sentence_length
        else:
            chunk.append(sentence)
            chunk_length += sentence_length
    # After iterating over all sentences, yield the final chunk
    yield " ".join(chunk) if chunk else ""


def print_preprocess_infos(input_text: str, chunks: List[str]) -> None:
    """
    Prints information about the input text and its chunks after preprocessing.

    Args:
        input_text (str): The original input text.
        chunks (str): A list of chunks obtained from the input text.

    Returns:
        None
    """
    print("------------------")
    # Delete extra spaces gathered during generate_chunks
    input_text_with_spaces = input_text.replace(
        ".", ". ").replace("?", "? ").replace("!", "! ")
    print(
        f"Input text contains {len(input_text_with_spaces)-(len(chunks)-1)} characters.")
    print("------------------")
    print(f"Found {len(chunks)} chunks!")
    print(f"Sizes: {[len(s) for s in chunks]} characters each.")
    print("------------------")


def get_input_textarea_element(driver: webdriver.Remote) -> WebElement:
    """
    Retrieves the input textarea element from the browser.

    Args:
        driver (webdriver): The browser instance.

    Returns:
        WebElement: The input textarea element.
    """
    return WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, INPUT_AREA)))


def translate_text(driver: webdriver.Remote, input_field: WebElement, chunks: list) -> list:
    """
    Translates a list of text chunks using the browser.

    Args:
        driver (webdriver): The browser instance.
        input_field (WebElement): The input textarea element.
        chunks (list): A list of text chunks to translate.

    Returns:
        list: A list of translated text chunks.
    """
    translation = []
    for index, chunk in enumerate(chunks):
        print(f"Translating chunk {index+1} of {len(chunks)}")
        print("------------------")
        input_field.send_keys(chunk)
        print("Fetching translation...")
        time.sleep(SLEEP_TIME)

        translated_chunk = driver.find_element(
            By.CSS_SELECTOR, OUTPUT_AREA).text

        translation.append(str(translated_chunk))
        input_field.clear()
    return translation


def write_output_file(file_name: str, translation: list) -> None:
    """
    Writes a list of translated text chunks to a file.

    Args:
        file_name (str): The name of the file to write.
        translation (list): A list of translated text chunks.
    """
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(translation)


# ---------------------------------------------------------------------------
# Main Code
def main() -> None:
    """
    Main entry point of the script.
    """
    driver = initialize_browser()
    print("Browser initialized")

    driver.get(LINK)

    print("Preprocessing data...")
    time.sleep(SLEEP_TIME)

    input_text = load_input_file(INPUT_FILE)
    sentences = split_text_into_sentences(input_text)
    chunks = list(generate_chunks(sentences))
    if PRINT_DETAILS:
        print_preprocess_infos(input_text, chunks)

    input_field = get_input_textarea_element(driver)
    translation = translate_text(driver, input_field, chunks)

    print("writing results to file...")
    write_output_file(OUTPUT_FILE, translation)

    driver.close()
    print("File written and browser shut down.\nTranslation successful.")


if __name__ == "__main__":
    main()
