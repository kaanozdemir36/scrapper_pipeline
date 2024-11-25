# Lonca Case Study - Product Entry

This project is a simplified version of a scraper pipeline for extracting product data from XML files and storing it in a MongoDB collection. 
It ensures seamless periodic updates without duplicating existing products.

## Requirements

- Python 3.10+
- MongoDB

## Usage

To process the XML file and store products in MongoDB:

1. Ensure MongoDB is running locally on your machine.
2. Place the XML file in the `data/` directory. The default file is `lonca-sample.xml`.
3. Run the `main.py` script to process and upload product data to MongoDB.

```bash
python main.py
```

To query the MongoDB collection:

1. Open your MongoDB client or shell.
2. Connect to the `lonca_case` database.
3. Use the `products` collection to view the data.

```bash
use scrapper_pipeline
db.products.find().pretty()
```

## Known Issues / Roadmap


- Implement support for processing multiple XML files simultaneously.
- Add logging for better traceability.
- Optimize product deduplication for large XML files.

## Bug Tracker


Bugs are tracked on `GitHub Issues <https://github.com/kaanozdemir36/scrapper_pipeline/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/kaanozdemir36/scrapper_pipeline/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.

## Authors

- **KAAN ÖZDEMİR**

## Maintainers


This project is maintained by the Kaan Özdemir.

You are welcome to contribute. To learn how please visit https://github.com/kaanozdemir36/scrapper_pipeline.
