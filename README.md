# UPAR 2027 Challenge Development Data @ Real-World Surveillance Workshop 2027

This repository prepares the public training and validation data for the two
UPAR 2027 Challenge tracks:

1. Pedestrian Attribute Recognition
2. Attribute-based Person Retrieval

Both tracks use the same ordered vocabulary of 40 binary attributes across
Market1501, PA-100K, and PETA.

## Information
Challenge Track 1: [Track 1]()

Challenge Track 1: [Track 2]()

Associated workshop: [Real-World Surveillance: Applications and Challenges Workshop](https://vap.aau.dk/rws)

Challenge results 2024: [UPAR@RWS2024](https://openaccess.thecvf.com/content/WACV2024W/RWS/papers/Cormier_UPAR_Challenge_2024_Pedestrian_Attribute_Recognition_and_Attribute-Based_Person_Retrieval_WACVW_2024_paper.pdf)

Challenge results 2023: [UPAR@RWS2023](https://openaccess.thecvf.com/content/WACV2023W/RWS/papers/Cormier_UPAR_Challenge_Pedestrian_Attribute_Recognition_and_Attribute-Based_Person_Retrieval_--_WACVW_2023_paper.pdf)

Challenge dataset: [UPAR dataset](https://openaccess.thecvf.com/content/WACV2023/papers/Specker_UPAR_Unified_Pedestrian_Attribute_Recognition_and_Person_Retrieval_WACV_2023_paper.pdf)

Original UPAR dataset: [Github](https://github.com/speckean/upar_dataset)

## Setup

```bash
conda env create -f environment.yml
conda activate rws-upar-challenge
python download_datasets.py
```

## Generated Structure

```text
.
│── data/                               
│   ├── annotations/                     
│   │   │── task1/                    
│   │   │   └── train/
│   │   │       └── gt.csv        -> attribute annotations for train split
│   │   │   └── val/
│   │   │       └── gt.csv        -> attribute annotations for val split
│   │   ├── task2/              
│   │   │   └── train/
│   │   │       └── gt.csv        -> attribute annotations
│   │   │       └── ids.csv       -> semantic ids for retrieval
│   │   │       └── queries.csv   -> attribute queries for the semantic ids
│   │   │   └── val/
│   │   │       └── gt.csv        -> attribute annotations
│   │   │       └── ids.csv       -> semantic ids for retrieval
│   │   │       └── queries.csv   -> attribute queries for the semantic ids
│   ├── Market1501/               -> Market1501 dataset
│   │   ├── bounding_box_test/
│   │   ├── bounding_box_train/
│   │   ├── query/
│   │   └── ...
│   ├── PA100k/                   -> PA100k dataset
│   │   └── release_data/
│   │       └── release_data/
│   └── PETA/                     -> PETA dataset
│       └── images/
└── submission_templates/
    ├── task1/                    -> submission template for task1
    └── task2/                    -> submission template for task2

```

`gt.csv` uses the challenge format `# image,<40 attributes>`. For retrieval,
each distinct 40-bit attribute vector is one query and `ids.csv` maps every
image to its zero-based query row. Train and validation query vocabularies are
kept separate.

Current release counts:

| Split | Images | Retrieval queries | Market1501 | PA100k | PETA |
|---|---:|---:|---:|---:|---:|
| Train | 97,669 | 7,204 | 10,000 | 79,001 | 8,668 |
| Validation | 33,407 | 3,462 | 16,458 | 9,986 | 6,963 |

## Dataset Sources
We build on an extension of the UPAR dataset.
The challenge training dataset consists of the harmonization of three public datasets (PA100K, PETA, and Market1501-Attributes) and a private test set.
40 binary attributes have been unified between those for which we provide additional annotations.
This dataset enables the investigation of Pedestrian Attribute Recognition (PAR) methods' generalization ability under different attribute distributions, viewpoints, varying illumination, and low resolutions.

If you use the UPAR dataset, please cite our UPAR papers as well as the papers of the sub-datasets:
- PA-100K: X. Liu et al., *HydraPlus-Net*, ICCV 2017, CC BY 4.0.
- PETA: Y. Deng et al., *Pedestrian Attribute Recognition at Far Distance*,
  ACM Multimedia 2014, research use only.
- Market1501: L. Zheng et al., *Scalable Person Re-identification: A
  Benchmark*, ICCV 2015.

```bibtex
@inproceedings{specker2023upar,
  title={UPAR: Unified Pedestrian Attribute Recognition and Person Retrieval},
  author={Specker, Andreas and Cormier, Mickael and Beyerer, Jurgen},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  year={2023}
}

@inproceedings{cormier2023upar,
  title={UPAR challenge: pedestrian attribute recognition and attribute-based person retrieval-dataset, design, and results},
  author={Cormier, Mickael and Specker, Andreas and Jacques, Julio CS and Florin, Lucas and Metzler, J{\"u}rgen and Moeslund, Thomas B and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J{\"u}rgen},
  booktitle={2023 IEEE/CVF Winter Conference on Applications of Computer Vision Workshops (WACVW)},
  pages={166--175},
  year={2023},
  organization={IEEE}
}

@inproceedings{cormier2024upar,
  title={Upar challenge 2024: Pedestrian attribute recognition and attribute-based person retrieval-dataset, design, and results},
  author={Cormier, Mickael and Specker, Andreas and Junior, Julio and CS, Jacques and Moritz, Lennart and Metzler, J{\"u}rgen and Moeslund, Thomas B and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J{\"u}rgen},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={359--367},
  year={2024}
}
```

## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>. The source image
datasets retain their respective licenses and usage restrictions.