# SimpleCalculator

## Steps

Run `pip install -r requirement.txt` to install all the libraries in the requirement file.

Create `.env` file and add `CONFIG_TYPE = 'settings.config.DevelopmentConfig'`. For production configuration make 
necessary changes in `settings/config.py` replace `CONFIG_TYPE = 'settings.config.ProductionConfig'` 

Run `python main.py`. Flask will open a port at http://0.0.0.0:8080/. You can also parse optional command line argument, 
`python main.py --host=0.0.0.0 --port=8080`. Click the link to generate the xlsx file. 

Check output in Binary Storage as `submission.xlsx`.

To run testcases `python tests/calc_tests.py`.

### Information

Final output in location `/binary_storage/submission.xlsx`.

Test plan in location `tests/TestPlan/`.

ER diagram in location `modules/calculator/ER/`.
