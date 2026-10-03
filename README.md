# TranslateModel

AI-assisted vernacular pedagogy and real-time translation for mother-tongue-based primary education.

## Problem Statement

**SIH26042 — AI-Powered Vernacular Pedagogy and Real-Time Translation Tool for Mother Tongue-Based Primary Education**

Jharkhand's PALASH Mother Tongue-Based Multilingual Education (MTB-MLE) programme has shown measurable improvements in foundational literacy among tribal children. However, scaling the programme is constrained by a shortage of teachers proficient in tribal languages such as **Ho, Mundari, and Santhali**. Most teachers assigned to tribal-area primary schools are trained in Hindi-medium instruction and need practical language tools to deliver lessons in the language children understand at home.

TranslateModel addresses this gap by providing an offline-first translation and curriculum-support platform for primary-school teachers. The intended system translates Hindi Foundational Literacy and Numeracy (FLN) content into tribal languages, supports classroom voice interaction, and generates bilingual learning materials suitable for low-connectivity environments.

## Proposed Solution

The project is designed as a software suite with the following capabilities:

- **Hindi-to-tribal-language translation** for lesson scripts, activity instructions, assessment prompts, and other FLN content.
- **Context-aware curriculum translation** using language-specific preprocessing and postprocessing.
- **Text-to-speech output** for translated classroom content.
- **Real-time voice-to-voice translation** so a Hindi-speaking teacher can interact with tribal-language-speaking students, with a target latency of no more than three seconds.
- **Automatic bilingual worksheet generation** aligned with NIPUN Bharat foundational learning outcomes.
- **Visual flashcard generation** for classroom vocabulary and activities.
- **Offline operation** after initial model and content synchronisation, targeting low-cost Android tablets with Android 9+ and approximately 2 GB RAM.

The current repository provides the translation-model foundation and a reproducible local inference workflow. The complete application will build on this foundation with speech, curriculum, worksheet, Android, and offline-sync components.

## Current Prototype Scope

The initial prototype demonstrates Hindi/Indic language model inference and is intended to be extended toward at least one target tribal language. IndicTrans2 language support includes **Santali (`sat_Olck`)**, which is a suitable first prototype target. Ho and Mundari support can be added through language-specific data, tokenizer/model support, terminology resources, and evaluation datasets as they become available.

> Translation quality for Ho and Mundari should not be assumed from the base model alone. These languages require curated parallel data, domain terminology, human review, and task-specific evaluation before classroom deployment.

## High-Level Workflow

```text
Hindi FLN content or teacher speech
              |
              v
   Text/speech input processing
              |
              v
 Hindi -> target tribal language translation
              |
       +------+------+
       |             |
       v             v
  Translated text   Synthesised audio
       |
       +----------------------+
       |                      |
       v                      v
 Bilingual worksheets    Classroom interaction
 and flashcards           (offline tablet)
```

## Repository Components

- `test_model.py` — local model inference/test entry point.
- `IndicTransToolkit/` — preprocessing, postprocessing, and evaluation utilities used by the translation pipeline.
- `indictrans2_model/` — model files/model-card information for the IndicTrans2-based translation component.
- `pyproject.toml` and `uv.lock` — Python project dependencies and reproducible environment lock data.

## Requirements

- Python 3.10 or newer.
- `uv` recommended for environment and dependency management.
- Linux or macOS for the current development workflow. Windows users may use WSL if required.
- Sufficient storage for the model and tokenizer files.
- GPU is optional for experimentation, but recommended for faster model inference. CPU inference can be used for functional testing.

## Recreate the Project from a Fresh Clone

These steps preserve the original repository setup process while making the model download and execution flow explicit.

### 1. Clone the repository

```bash
git clone https://github.com/ishu17077/TranslateModel.git
cd TranslateModel
```

### 2. Create a virtual environment

Using `uv`:

```bash
uv venv
```

Alternatively, using Python's built-in environment module:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

With `uv`:

```bash
uv sync
```

If the environment was created with `python -m venv`, activate it first and install the project dependencies according to `pyproject.toml`:

```bash
pip install -e .
```

### 5. Download or restore the quantized model

Download the quantized model artifact from the repository's **Releases** page and place it in the model location expected by the inference code. Keep large model binaries out of normal Git commits.

For development experiments that use a Hugging Face model rather than a packaged release artifact, ensure that the model and tokenizer are downloaded while internet access is available. After the files have been cached or copied to the tablet, inference can be adapted to run without network access.

### 6. Run the model test

```bash
python test_model.py
```

The test script should load the local model, run a translation example, and print the generated output. If the script expects a specific model path or filename, update its configuration to match the downloaded release artifact.

## Reproducing a Hindi-to-Santali Translation Experiment

The model language identifiers used by IndicTrans2 include:

- Hindi: `hin_Deva`
- Santali: `sat_Olck`

A typical experiment should follow this sequence:

1. Load the tokenizer and local model.
2. Preprocess Hindi input with the source language `hin_Deva` and target language `sat_Olck`.
3. Run generation with conservative sequence limits suitable for low-memory devices.
4. Decode and postprocess the output.
5. Compare the output with a human-reviewed reference translation.
6. Measure translation quality and latency on the target tablet.

For classroom use, add a terminology glossary for names, local places, classroom commands, numbers, and FLN vocabulary. Human review is required before using generated content with children.

## Application Development Plan

The repository can be extended into the complete SIH solution in the following stages:

1. **Translation foundation** — package the model and tokenizer for offline inference and add Hindi-to-Santali test data.
2. **Language resources** — collect and validate parallel Hindi–Ho, Hindi–Mundari, and Hindi–Santali FLN content with native-speaker review.
3. **Speech pipeline** — add offline Hindi speech recognition, translation, and tribal-language text-to-speech; measure end-to-end latency with a target below three seconds.
4. **Curriculum tools** — convert NIPUN Bharat learning outcomes into structured lesson templates, bilingual worksheets, assessment prompts, and flashcards.
5. **Android deployment** — export or integrate a quantized model suitable for Android 9+ devices with approximately 2 GB RAM.
6. **Offline synchronisation** — provide one-time content/model synchronisation, local storage, versioning, and optional update packages for areas with intermittent connectivity.
7. **Evaluation and demo** — test translation quality with native speakers, verify offline behavior, benchmark latency and memory, and record the required demonstration video.

## Evaluation Checklist

A prototype demonstration should document:

- Hindi-to-tribal-language translation accuracy, preferably with native-speaker ratings and BLEU/ChrF or comparable metrics.
- Speech recognition, translation, and speech synthesis latency, including the percentage of interactions completed within three seconds.
- Memory usage and model size on a low-cost Android 9+ tablet with approximately 2 GB RAM.
- Successful inference with Wi-Fi/mobile data disabled after initial synchronisation.
- Quality and alignment of generated bilingual worksheets and flashcards with the selected NIPUN Bharat learning outcomes.
- Handling of uncertain translations, unsupported language content, and teacher correction feedback.

## Responsible Use

This system is an educational aid, not a replacement for teachers or native-language experts. All lesson content, translations, audio, worksheets, and assessments should be reviewed by qualified educators and fluent speakers before classroom distribution. Avoid collecting unnecessary student voice recordings or personally identifiable information, and provide clear feedback when the model is uncertain.

## Project Status

The repository currently focuses on the translation-model setup and test workflow. Speech translation, automated worksheet/flashcard generation, Android packaging, and full offline synchronisation are the next application-level integration steps required for the complete SIH26042 solution.
