Software that will facilitate multi-head 3D Printer control, provide print time duration estimates, and calulculate energy and material consumption.

Steps:
- Finished a Python Script that scrapes G-Code files, processes their data and converts them to JSON, according to company needs.
- Implement tests, to see if all JSON printed products match the Original G-Code printed products.
- Once all tests are passed, implement some CI (maybe with GitHub Actions) to automatically run all tests whenever new code is pushed to master, to ensure quality and guarantee that no new code compromises product integrity.
- Create a function to estimate print time, material consumption and energy consumption based on factors like motor strength and print head acceleration.
