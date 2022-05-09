fields = [('tech', 'Technology'), ('eng', 'Engineering'), ('bio', 'Biology'), ('art', 'Art'), ('ath', 'Athletics'),
          ('fin', 'Finance'), ('bus', 'Business')]
cities = [("bos", "Boston, MA"), ("ny", "New York, NY"), ("chic", "Chicago, IL"), ("phil", "Philadelphia, PA"),
          ("hous", "Houston, TX"),
          ("phnx", "Phoenix, AZ"), ("sea", "Seattle, WA"), ("mia", "Miami, FL")]
education_choices = [
    ("hs", "High School"),
    ("ud", "Undergrad"),
    ("gd", "graduate")
]
salary_options = [50000, 75000, 100000, 150000, 175000, 200000, 250000, 805000]
jobs = [
    {
        "company": "BitSight",
        "position": "Entry Software Engineer",
        "salary": 100000,
        "interests": ["tech"],
        "locations": ["bos", "sea"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."
    },
    {
        "company": "Brigham and Women's",
        "position": "Neuroscientist",
        "salary": 300000,
        "interests": ["tech", "bio"],
        "locations": ["ny", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Ai Proteins",
        "position": "protein expert",
        "salary": 500000,
        "interests": ["bio"],
        "locations": ["mia"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Ai Proteins",
        "position": "test Subject",
        "salary": 50000,
        "interests": ["bio", "ath"],
        "locations": ["phil", "hous", "phnx"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Flux marine",
        "position": "Junior Software Engineer",
        "salary": 150000,
        "interests": ["tech", "eng"],
        "locations": ["phil", "hous", "phnx", "bos", "ny", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Fritz",
        "position": "Senior Software Engineer",
        "salary": 200000,
        "interests": ["tech"],
        "locations": ["phil", "hous", "ny", "mia"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Heartifyio",
        "position": "Entry Software Developer",
        "salary": 100000,
        "interests": ["tech", "bio"],
        "locations": ["hous", "ny", "mia"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "RH",
        "position": "AI engineer",
        "salary": 100000000,
        "interests": ["tech", "art"],
        "locations": ["phil", "hous", "mia"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Isomics",
        "position": "Senior coach",
        "salary": 100000,
        "interests": ["tech", "ath"],
        "locations": ["bos"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."
    },
    {
        "company": "Ultimaco",
        "position": "Senior CyberSecurity Expert",
        "salary": 300000,
        "interests": ["tech", "bus", "eng"],
        "locations": ["chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Ultimaco",
        "position": "Senior CyberSecurity Expert",
        "salary": 300000,
        "interests": ["tech", "bus", "eng"],
        "locations": ["mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Ultimaco",
        "position": "Entry Software engineer",
        "salary": 100000,
        "interests": ["tech"],
        "locations": ["ny", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Ultimaco",
        "position": "Senior CyberSecurity Expert",
        "salary": 300000,
        "interests": ["tech", "bus", "eng"],
        "locations": ["phil", "hous", "bos", "ny", ],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "CompBioLab",
        "position": "Bioinformatics Expert",
        "salary": 200000,
        "interests": ["tech", "bio"],
        "locations": ["phnx", "bos", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "HourWork",
        "position": "Junior Software Engineer",
        "salary": 150000,
        "interests": ["tech"],
        "locations": ["phnx"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "HourWork",
        "position": "Senior Software Engineer",
        "salary": 300000,
        "interests": ["tech"],
        "locations": ["phil", "hous", "phnx", "bos", "ny", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                        "labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. "
                        "Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam "
                        "malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur "
                        "adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis "
                        "rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida "
                        "arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies. "

    },
    {
        "company": "NYU Langone Health",
        "position": "Financial Adivisor",
        "salary": 800000,
        "interests": ["tech", "fin"],
        "locations": ["phil", "phnx", "bos", "ny"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "NYU Langone Health",
        "position": "Doctor",
        "salary": 800000,
        "interests": ["bio"],
        "locations": ["bos", "ny", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "FC Barcelona",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phil", "hous", "phnx"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "New York Knicks",
        "position": "Coach",
        "salary": 600000,
        "interests": ["ath"],
        "locations": ["phil", "hous", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Dallas Cowboys",
        "position": "Coach",
        "salary": 900000,
        "interests": ["ath"],
        "locations": ["mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Los Angeles Lakers",
        "position": "Coach",
        "salary": 1000000,
        "interests": ["ath"],
        "locations": ["phil", "bos", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."
    },
    {
        "company": "Boston Celtics",
        "position": "Coach",
        "salary": 700000,
        "interests": ["ath"],
        "locations": ["ny", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."
    },
    {
        "company": "New York Jets",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phnx", "bos"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Boston Red Sox",
        "position": "Coach",
        "salary": 1500000,
        "interests": ["ath"],
        "locations": ["hous"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Manchester United F.C.",
        "position": "Coach",
        "salary": 160000000,
        "interests": ["ath"],
        "locations": ["bos", "ny", "mia"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Atlanta Falcons",
        "position": "Coach",
        "salary": 9000000,
        "interests": ["ath"],
        "locations": ["phil", "hous", "phnx"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "FC Bayern Munich",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phil", "hous", ],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Liverpool F.C.",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phnx", "bos", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Real Madrid CF",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["bos", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Brooklyn Nets",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phil", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Chicago Cubs",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phil", "phnx", "ny", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
    {
        "company": "Los Angeles Chargers",
        "position": "Coach",
        "salary": 800000,
        "interests": ["ath"],
        "locations": ["phil", "hous", "bos", "ny", "mia", "chic"],
        "descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Sit amet consectetur adipiscing elit ut aliquam purus sit amet. Nec sagittis aliquam malesuada bibendum. Massa eget egestas purus viverra. Ipsum dolor sit amet consectetur adipiscing. Lacus sed viverra tellus in hac habitasse platea. Sagittis nisl rhoncus mattis rhoncus urna. Senectus et netus et malesuada fames ac turpis egestas. Non curabitur gravida arcu ac tortor dignissim convallis. Vestibulum lorem sed risus ultricies."

    },
]
groups = [
    {
        "name": "jobSeeker"
    },
    {
        "name": "employer"
    },
]
users = [
    {
        "first_name": "Shujaullah",
        "last_name": "Ahsan",
        "username": "shuja12",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Krishna",
        "last_name": "Patel",
        "username": "Krishnap",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Jacob",
        "last_name": "Redd",
        "username": "ReddJ",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Lady",
        "last_name": "Feet",
        "username": "FeetLover123",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Malania",
        "last_name": "Miquella",
        "username": "Blade",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Leonel",
        "last_name": "Messi",
        "username": "Messi10",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Cristiano",
        "last_name": "Ronaldo",
        "username": "R7",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "karim",
        "last_name": "Benzema",
        "username": "BigBenz",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Kyle",
        "last_name": "jackson",
        "username": "Mongraal",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },
    {
        "first_name": "Ronaldinho",
        "last_name": "Gaucho",
        "username": "BestSkiller",
        "email": "shujaullah.ahsan001@umb.edu",
        "password1": "RedCar123@",
        "password2": "RedCar123@",
        "position": "jobSeeker",
    },

]
education = [
    {
        "title": "Bachelors in Computer Science",
        "school": "Boston College",
        "tuition": 35000,
        "locations": ["ny"],
        "interests": ["tech"]
    },
    {
        "title": "Associates in Business Management",
        "school": "UMASS Lowell",
        "tuition": 35000,
        "locations": ["ny", "mia"],
        "interests": ["bus"]
    },
    {
        "title": "Associates in Arts",
        "school": "UMASS Amherst",
        "tuition": 35000,
        "interests": ["art"],
        "locations": ["ny", "sea"],
    },
    {
        "title": "Associates in Health Care Management",
        "school": "UMASS Boston",
        "tuition": 54000,
        "interests": ["bio"],
        "locations": ["bos", "chi"],
    },

]
