# DeepL Translator Script

**Translate effortlessly: automate text translations with the DeepL service using Selenium.**

![Banner Image](/img/banner-img.jpg "A banner image depicting a cat playing on the tower of Babel.")
*Pastiche by FatCatArt inspired by Pieter Bruegel the elder's tower of Babel.*

### Genesis

>The idea occured while translating news articles from multiple languages. This was a real pain point on a recent personal project: the restrictive character limit made it difficult to get an overview of the full article. This script provides a way to get a better translation experience at once without having to tediously copy and paste the translated text chunks. A real time-saver :)

As a student I took this side project as an opportunity to discover automation using Selenium and implement some coding best practices learned at school.
The project not only solved an immediate problem, but also deepened my practical software development skills. If you are eager to learn more, dive into the code! The **tutorial** articles are available here:

* [Part I: setup](https://dev.to/atomictangerline/basic-selenium-the-easy-peasy-introduction-chapter-1-of-3-4fe3)
* [Part II: overview](https://dev.to/atomictangerline/basic-selenium-the-easy-peasy-introduction-chapter-2-of-3-1oad)
* [Part III: deep dive](https://dev.to/atomictangerline/basic-selenium-the-easy-peasy-introduction-chapter-3-of-3-3bb7)

**NB:** This script uses the [DeepL translation service](https://www.deepl.com/translator), which has usage limits and requires a subscription for heavy usage.

> [!NOTE]
> Be aware that in the constantly shifting landscape of website updates, this script may become disrupted unexpectedly. It was last verified to be functioning as of *February 2025*.

## Table of Content

<details>
<summary> Contents - click to expand</summary>

- [DeepL Translator Script](#deepl-translator-script)
    - [Genesis](#genesis)
  - [Table of Content](#table-of-content)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Limitations](#limitations)
  - [Troubleshooting](#troubleshooting)
  - [Further learning](#further-learning)
  - [Contributing](#contributing)
  - [Legal](#legal)
    - [License](#license)
    - [Acknowledgments](#acknowledgments)
    - [Disclaimer](#disclaimer)

</details>

## Requirements

* Python 3.x
* Selenium
* GeckoDriver [(available here)](https://github.com/mozilla/geckodriver/releases)

## Installation

1. Clone or download this repository.
2. If you don't have it yet, install Firefox on your system/environment. This is the command for debian-based distros like Ubuntu:

    ```bash
    sudo apt update && sudo apt install firefox
3. Install the required packages using pip:

   ```bash
    pip install -r requirements.txt
4. Download the GeckoDriver executable from the official Mozilla [repository](https://github.com/mozilla/geckodriver/), extract it to /opt (common practice) or any directory you prefer (update the directories accordingly), set the permissions and create symbolic links to make the webdriver available in the system's PATH.

   ```bash
    wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz \
    && sudo tar -C /opt -xzf /tmp/geckodriver.tar.gz \
    && sudo chmod 755 /opt/geckodriver \
    && sudo ln -fs /opt/geckodriver /usr/bin/geckodriver \
    && sudo ln -fs /opt/geckodriver /usr/local/bin/geckodriver

> [!NOTE]
>**WSL2 users:** In order to launch Firefox, it is possible set up Windows to run Linux GUI apps. Depending on your OS version, follow this [tutorial](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps) or this [one](https://aalonso.dev/blog/2021/how-to-use-gui-apps-in-wsl2-forwarding-x-server-cdj).

## Usage

1. Update the `INPUT_FILE` and `OUTPUT_FILE` parameters in the script to point to your input and output files. The script will process any file that contains *text*:

    * Plain text files (.txt)
    * Markdown files (.md)
    * HTML files (.html, .htm)
    * XML files (.xml)
    * JSON files (.json)
    * CSV files (.csv)  
    * *or any other type of file that contains text data.*
  
> [!IMPORTANT]
> The script *requires* an **input** file. If no **output** file exists at the specified location, a new one will be created; otherwise, the existing output file will be overwritten each time the script is run.

2. Run the script in the terminal:

    ```bash
    python translator.py
3. The script will translate the text found in the input file and write the translation to the output file (the output file will be created if it does not exist and overwritten otherwise).

## Configuration

The script uses the following configuration variables:

* `FIREFOX_PATH`: The path to the Firefox executable. Command to check its location (Linux/macOS):

    ```bash
    which firefox
* `GECKODRIVER_PATH`: The path to the GeckoDriver executable. It should be the one provided during the installation. You can check it with this command:

    ```bash
    which geckodriver
* `HEADLESS`: A boolean variable that determines whether to run the browser in headless mode.

* `SOURCE_LANG`: The source language of the text to translate (currently set to English (US)). For other available languages, see the list below.
* `OUTPUT_LANG`: The target language of the text to translate (currently set to French). For other available languages, see the list below.
* `CHAR_LIMIT`: Maximum character limit for each chunk of text to be translated (currently set to 1500 characters).
* `TIMEOUT`: The timeout in seconds for Selenium to wait for elements to load.
* `SLEEP_TIME`: The time in seconds to wait between translating each chunk of text.

<details>
<summary> List of supported languages (Nov. 2024):</summary>

| Language      | Language code|
| ------------- | ------------- |
| Arabic  | ar  |
| Bulgarian  | bg  |
| Chinese (simple) | zh-hans  |
| Chinese  (traditional)| zh-hant  |
| Czech  | cs  |
| Danish  | da  |
| Dutch  | nl  |
| English  | en  |
| English (US) | en-us  |
| Estonian  | et  |
| Finnish  | fi  |
| French  | fr  |
| German  | de  |
| Greek  | el  |
| Hungarian  | hu  |
| Indonesian  | id  |
| Italian  | it  |
| Japanese  | ja  |
| Korean  | ko  |
| Latvian  | lv  |
| Lithuanian  | lt  |
| Norwegian (Bokmål)  | nb  |
| Polish  | pl  |
| Portuguese  | pt-pt  |
| Portuguese (Brazil) | pt-br  |
| Romanian  | ro  |
| Russian  | ru  |
| Slovak  | sk  |
| Slovenian  | sl  |
| Spanish  | es  |
| Swedish  | sv  |
| Turkish  | tr  |
| Ukrainian  | uk  |

</details>

## Limitations

> [!WARNING]
> It's important to note that if you don't manually rename the output file variable after each run, the script will overwrite the previous file, causing you to lose its content.

The script was developed with Firefox in mind. If you are a Chrome user, you will have to modify the code to initiate an instance of [Chromedriver](https://developer.chrome.com/docs/chromedriver/downloads) instead of Geckodriver.

The script is intended as an educational side project, and is not meant for extensive use. If you use the script too frequently, you may quickly hit some usage limits potentially resulting in your IP address being blacklisted.

> [!TIP]
> As the script currently only supports processing a single input file at a time. The recommended approach is to gather all your source texts into a single file. You will then get them translated into one output file.

## Troubleshooting

If the script fails to launch the browser, check that the `FIREFOX_PATH` and `GECKODRIVER_PATH` variables are set correctly.

If the script fails to translate the text, check that the `SOURCE_LANG` and `OUTPUT_LANG` variables are set correctly.

If the script fails to write the translated text to the output file, check that the `OUTPUT_FILE` variable is set correctly.

If the script translates the text into German instead of the specified `OUTPUT_LANG`. It's possible that the webdriver connects to the website but has not managed to switch languages (German is DeepL's default output language). Try adjusting the `SLEEP_TIME` to a higher value.

## Further learning

* A tutorial that inspired this project: [YouTube link](https://www.youtube.com/watch?v=aSeqMYNhEHo)
* The tutorial about this project: [Available here](https://dev.to/atomictangerline/series/30533)

## Contributing

Contributions are **welcome!** I appreciate your support: each contribution and feedback helps me grow and improve.

This project is intended as a practice on a real world use case, feel free to play with it. I'm open to any suggestion that will improve the code quality and deepen my software programming skills. If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Legal

### License

The source code is provided under a [Creative Commons CC0 license](https://creativecommons.org/publicdomain/zero/1.0/). See the [LICENSE](/LICENSE) file for details.

### Acknowledgments

This project uses the following libraries and services:

* [GeckoDriver](https://github.com/mozilla/geckodriver/releases): a WebDriver implementation for [Mozilla Firefox](https://mozilla.org/firefox)
* [Selenium's WebDriver](https://www.selenium.dev/documentation/webdriver/): a browser automation framework
* [DeepL](https://www.deepl.com/translator): an online (deep learning based) translation service

### Disclaimer

This project is not affiliated with DeepL or Mozilla. The use of the DeepL or any other translation service is subject to their terms and conditions.
