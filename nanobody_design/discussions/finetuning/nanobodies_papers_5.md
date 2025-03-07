## User

This is the beginning of an individual meeting with Immunologist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. You are responsible for understanding the topic "nanobodies" in the context of designing nanobody binders for SARS-CoV-2. You need to fine-tune yourself on the relevant literature on nanobodies to improve your ability to design SARS-CoV-2 nanobody binders. Please use PubMed Central and search for relevant papers on nanobodies using the query "broadly neutralizing nanobodies AND coronavirus" and request 100 articles with abstracts only. Read all of the abstracts and based on each abstract individually, decide whether you want to fine-tune yourself on the full text of that paper. Include as many papers as possible, but only include papers that are directly relevant to nanobodies. Please provide the PMCIDs and titles of all the papers that you wish to fine-tune yourself on as a Python dictionary mapping PMCID as a double-quoted string to title as a double-quoted string.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Immunologist, please provide your response to the agenda.

## Immunologist

Based on the abstracts provided, I have selected the following papers that are directly relevant to the topic of nanobodies and their application in neutralizing SARS-CoV-2 and its variants. Here is the Python dictionary mapping PMCID to title:

```python
{
    "11140877": "Therapeutic nanobodies against SARS-CoV-2 and other pathogenic human coronaviruses",
    "7224157": "Identification of Human Single-Domain Antibodies against SARS-CoV-2",
    "9797221": "Therapeutic applications of nanobodies against SARS-CoV-2 and other viral infections: Current update",
    "8907017": "Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody",
    "8768012": "Bovine-derived antibodies and camelid-derived nanobodies as biotherapeutic weapons against SARS-CoV-2 and its variants: A review article",
    "8514607": "The role of single-domain antibodies (or nanobodies) in SARS-CoV-2 neutralization",
    "10268213": "Fully synthetic platform to rapidly generate tetravalent bispecific nanobody–based immunoglobulins",
    "8651292": "Highly synergistic combinations of nanobodies that target SARS-CoV-2 and are resistant to escape",
    "11076045": "Nanobody repertoire generated against the spike protein of ancestral SARS-CoV-2 remains efficacious against the rapidly evolving virus",
    "8956255": "Multivariate mining of an alpaca immune repertoire identifies potent cross-neutralizing SARS-CoV-2 nanobodies",
    "8951411": "Structural and Computational Studies of the SARS-CoV-2 Spike Protein Binding Mechanisms with Nanobodies: From Structure and Dynamics to Avidity-Driven Nanobody Engineering",
    "9801699": "Applications of nanobodies in the prevention, detection, and treatment of the evolving SARS-CoV-2",
    "9792944": "Broadly neutralizing and protective nanobodies against SARS-CoV-2 Omicron subvariants BA.1, BA.2, and BA.4/5 and diverse sarbecoviruses",
    "10715488": "Identification of nurse shark VNAR single-domain antibodies targeting the spike S2 subunit of SARS-CoV-2",
    "9219022": "Production and purification of shark and camel single domain antibodies from bacterial and mammalian cell expression systems",
    "11148044": "Generation of nanobodies from transgenic ‘LamaMice’ lacking an endogenous immunoglobulin repertoire",
    "11460708": "Structure-guided in vitro evolution of nanobodies targeting new viral variants",
    "9351521": "Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes",
    "10865538": "Single-domain antibodies against SARS-CoV-2 RBD from a two-stage phage screening of universal and focused synthetic libraries",
    "9170159": "Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants",
    "7857409": "An ultrapotent synthetic nanobody neutralizes SARS-CoV-2 by stabilizing inactive Spike",
    "11659936": "Single domain antibody: Development and application in biotechnology and biopharma",
    "9884143": "Expanding and improving nanobody repertoires using a yeast display method: Targeting SARS-CoV-2",
    "11108896": "Nanobodies in the fight against infectious diseases: repurposing nature's tiny weapons",
    "10968798": "Aptamers and Nanobodies as New Bioprobes for SARS-CoV-2 Diagnostic and Therapeutic System Applications",
    "10373554": "Broad Sarbecovirus Neutralizing Antibodies Obtained by Computational Design and Synthetic Library Screening",
    "8908544": "Structural basis of nanobodies neutralizing SARS-CoV-2 variants",
    "10444775": "Discovery and multimerization of cross-reactive single-domain antibodies against SARS-like viruses to enhance potency and address emerging SARS-CoV-2 variants",
    "10878242": "A novel strategy for an anti-idiotype vaccine: nanobody mimicking neutralization epitope of porcine circovirus type 2",
    "7199733": "Structural Basis for Potent Neutralization of Betacoronaviruses by Single-Domain Camelid Antibodies",
    "11407660": "Dual-role epitope on SARS-CoV-2 spike enhances and neutralizes viral entry across different variants",
    "7857400": "Versatile and multivalent nanobodies efficiently neutralize SARS-CoV-2",
    "9257560": "A panel of nanobodies recognizing conserved hidden clefts of all SARS-CoV-2 spike variants including Omicron",
    "8625641": "Structural Biology of Nanobodies against the Spike Protein of SARS-CoV-2",
    "11285730": "Structural and functional characterization of nanobodies that neutralize Omicron variants of SARS-CoV-2",
    "8924699": "Recombinant Limosilactobacillus (Lactobacillus) delivering nanobodies against Clostridium perfringens NetB and alpha toxin confers potential protection from necrotic enteritis",
    "11554226": "Super broad and protective nanobodies against Sarbecoviruses including SARS-CoV-1 and the divergent SARS-CoV-2 subvariant KP.3.1.1",
    "8021111": "Dromedary camels as a natural source of neutralizing nanobodies against SARS-CoV-2",
    "9356539": "Rapid and Quantitative In-vitro Evaluation of SARS-CoV-2 Neutralizing Antibodies and Nanobodies",
    "10167778": "Isolation and characterization of single domain antibodies from banded houndshark (Triakis scyllium) targeting SARS-CoV-2 spike RBD protein",
    "7642257": "Perspective: Reducing SARS-CoV2 Infectivity and Its Associated Immunopathology",
    "9461429": "Arsenal of nanobodies shows broad-spectrum neutralization against SARS-CoV-2 variants of concern in vitro and in vivo in hamster models",
    "8458290": "A potent SARS-CoV-2 neutralising nanobody shows therapeutic efficacy in the Syrian golden hamster model of COVID-19",
    "9482557": "Single domain antibodies derived from ancient animals as broadly neutralizing agents for SARS-CoV-2 and other coronaviruses",
    "7112682": "Use of camel single-domain antibodies for the diagnosis and treatment of zoonotic diseases",
    "11211474": "A broad neutralizing nanobody against SARS-CoV-2 engineered from an approved drug",
    "9150821": "Anti-HIV-1 Nanobody-IgG1 Constructs With Improved Neutralization Potency and the Ability to Mediate Fc Effector Functions",
    "10955499": "Plant virus‐derived nanoparticles decorated with genetically encoded SARS‐CoV‐2 nanobodies display enhanced neutralizing activity",
    "9411660": "Research progress and applications of nanobody in human infectious diseases",
    "10590698": "Nanobodies with cross-neutralizing activity provide prominent therapeutic efficacy in mild and severe COVID-19 rodent models",
    "8333356": "Potent neutralizing nanobodies resist convergent circulating variants of SARS-CoV-2 by targeting diverse and conserved epitopes",
    "10833066": "NanoLAS: a comprehensive nanobody database with data integration, consolidation and application",
    "11515141": "Discovery of nanobodies: a comprehensive review of their applications and potential over the past five years",
    "11054741": "Engineered Multivalent Nanobodies Efficiently Neutralize SARS-CoV-2 Omicron Subvariants BA.1, BA.4/5, XBB.1 and BQ.1.1",
    "8699001": "Central Nervous System Delivery of Antibodies and Their Single-Domain Antibodies and Variable Fragment Derivatives with Focus on Intranasal Nose to Brain Administration",
    "11347438": "A single domain antibody-based Luminex assay for the detection of SARS-CoV-2 in clinical samples",
    "6640686": "Single-Domain Antibodies and Their Formatting to Combat Viral Infections",
    "11609455": "Nanobodies: From High-Throughput Identification to Therapeutic Development",
    "10891761": "Serial Llama Immunization with Various SARS-CoV-2 RBD Variants Induces Broad Spectrum Virus-Neutralizing Nanobodies",
    "7854682": "Anti-CfaE nanobodies provide broad cross-protection against major pathogenic enterotoxigenic Escherichia coli strains, with implications for vaccine design",
    "8463502": "Rapid generation of potent antibodies by autonomous hypermutation in yeast",
    "8324831": "A synthetic nanobody targeting RBD protects hamsters from SARS-CoV-2 infection",
    "8043454": "Nanobody Repertoires for Exposing Vulnerabilities of SARS-CoV-2",
    "8465657": "A Small Virus to Deliver Small Antibodies: New Targeted Therapies Based on AAV Delivery of Nanobodies",
    "8811630": "Biparatopic nanobodies protect mice from lethal challenge with SARS‐CoV‐2 variants of concern",
    "8928829": "Nebulized delivery of a broadly neutralizing SARS-CoV-2 RBD-specific nanobody prevents clinical, virological, and pathological disease in a Syrian hamster model of COVID-19",
    "9063451": "Neutralizing Dromedary-Derived Nanobodies Against BotI-Like Toxin From the Most Hazardous Scorpion Venom in the Middle East and North Africa Region",
    "10518403": "Unleashing the power of shark variable single domains (VNARs): broadly neutralizing tools for combating SARS-CoV-2",
    "8828845": "An ultrapotent RBD-targeted biparatopic nanobody neutralizes broad SARS-CoV-2 variants",
    "9529347": "Biparatopic nanobodies targeting the receptor binding domain efficiently neutralize SARS-CoV-2",
    "9174178": "Superimmunity by pan-sarbecovirus nanobodies",
    "10588750": "A Naïve Phage Display Library-Derived Nanobody Neutralizes SARS-CoV-2 and Three Variants of Concern",
    "9896449": "Shark nanobodies with potent SARS-CoV-2 neutralizing activity and broad sarbecovirus reactivity",
    "7430568": "An ultra-potent synthetic nanobody neutralizes SARS-CoV-2 by locking Spike into an inactive conformation",
    "10054972": "Nanobodies against SARS-CoV-2 reduced virus load in the brain of challenged mice and neutralized Wuhan, Delta and Omicron Variants",
    "5754017": "Using Homology Modeling to Interrogate Binding Affinity in Neutralization of Ricin Toxin by a Family of Single Domain Antibodies",
    "10858526": "Targeted drug delivery using nanobodies to deliver effective molecules to breast cancer cells: the most attractive application of nanobodies",
    "10275483": "Emerging Landscape of Nanobodies and Their Neutralizing Applications against SARS-CoV-2 Virus",
    "9113008": "SARS-CoV-2 Delta Variant Decreases Nanobody Binding and ACE2 Blocking Effectivity",
    "11228696": "Current development of severe acute respiratory syndrome coronavirus 2 neutralizing antibodies (Review)",
    "9132424": "Deep mutational engineering of broadly-neutralizing nanobodies accommodating SARS-CoV-1 and 2 antigenic drift",
    "8451865": "Development of a platform process for the production and purification of single‐domain antibodies",
    "10597523": "Computational design of novel nanobodies targeting the receptor binding domain of variants of concern of SARS-CoV-2",
    "8700021": "Epitope profiling using computational structural modelling demonstrated on coronavirus-binding antibodies"
}
```

These papers provide comprehensive insights into the development, engineering, and application of nanobodies for neutralizing SARS-CoV-2 and its variants, which are directly relevant to your research project.

## User

Tool Output:

Here are the top 100 articles on PubMed Central for the query "broadly neutralizing nanobodies AND coronavirus":

[begin paper 1]

PMCID = 11140877

Title = Therapeutic nanobodies against SARS-CoV-2 and other pathogenic human coronaviruses

Nanobodies, single-domain antibodies derived from variable domain of camelid or shark heavy-chain antibodies, have unique properties with small size, strong binding affinity, easy construction in versatile formats, high neutralizing activity, protective efficacy, and manufactural capacity on a large-scale. Nanobodies have been arisen as an effective research tool for development of nanobiotechnologies with a variety of applications. Three highly pathogenic coronaviruses (CoVs), SARS-CoV-2, SARS-CoV, and MERS-CoV, have caused serious outbreaks or a global pandemic, and continue to post a threat to public health worldwide. The viral spike (S) protein and its cognate receptor-binding domain (RBD), which initiate viral entry and play a critical role in virus pathogenesis, are important therapeutic targets. This review describes pathogenic human CoVs, including viral structures and proteins, and S protein-mediated viral entry process. It also summarizes recent advances in development of nanobodies targeting these CoVs, focusing on those targeting the S protein and RBD. Finally, we discuss potential strategies to improve the efficacy of nanobodies against emerging SARS-CoV-2 variants and other CoVs with pandemic potential. It will provide important information for rational design and evaluation of therapeutic agents against emerging and reemerging pathogens.

[end paper 1]

[begin paper 2]

PMCID = 7224157

Title = Identification of Human Single-Domain Antibodies against SARS-CoV-2

The worldwide spread of COVID-19 highlights the need for an efficient approach to rapidly develop therapeutics and prophylactics against SARS-CoV-2. The SARS-CoV-2 spike protein, containing the receptor-binding domain (RBD) and S1 subunit involved in receptor engagement, is a potential therapeutic target. We describe the development of a phage-displayed single-domain antibody library by grafting naive complementarity-determining regions (CDRs) into framework regions of a human germline immunoglobulin heavy chain variable region (IGHV) allele. Panning this library against SARS-CoV-2 RBD and S1 subunit identified fully human single-domain antibodies targeting five distinct epitopes on SARS-CoV-2 RBD with subnanomolar to low nanomolar affinities. Some of these antibodies neutralize SARS-CoV-2 by targeting a cryptic epitope located in the spike trimeric interface. Collectively, this work presents a versatile platform for rapid antibody isolation and identifies promising therapeutic anti-SARS-CoV-2 antibodies as well as the diverse immogneic profile of the spike protein.

A phage-displayed human single-domain antibody library is developed

Single-domain antibodies targeting five types of SARS-CoV-2 epitopes are identified

Some neutralizing antibodies target cryptic SARS-CoV-2 spike trimeric interface

Unique immunogenic profile of SARS-CoV-2 RBD is revealed

Wu et al. describe the development of a versatile platform for rapid isolation of fully human single-domain antibodies and apply this methodology to identify SARS-CoV-2-specific antibodies. These human single-domain antibodies target diverse epitopes within the SARS-CoV-2 spike protein receptor binding domain (RBD) and may yield potential therapeutic candidates for COVID-19.

[end paper 2]

[begin paper 3]

PMCID = 9797221

Title = Therapeutic applications of nanobodies against SARS-CoV-2 and other viral infections: Current update

In the last two years, the world encountered the SARS-CoV-2 virus, which is still dominating the population due to the absence of a viable treatment. To eradicate the global pandemic, scientists, doctors, and researchers took an exceptionally significant initiative towards the development of effective therapeutics to save many lifes. This review discusses about the single-domain antibodies (sdAbs), also called nanobodies, their structure, and their types against the infections of dreadful SARS-CoV-2 virus. A precise description highlights the nanobodies and their therapeutic application against the other selected viruses. It aims to focus on the extraordinary features of these antibodies compared to the conventional therapeutics like mAbs, convalescent plasma therapy, and vaccines. The stable structure of these nanobodies along with the suitable mechanism of action also confers greater resistance to the evolving variants with numerous mutations. The nanobodies developed against SARS-CoV-2 and its mutant variants have shown the greater neutralization potential than the primitive ones. Engineering of these specialized antibodies by modern biotechnological approaches will surely be more beneficial in treating this COVID-19 pandemic along with certain other viral infections.

[end paper 3]

[begin paper 4]

PMCID = 8907017

Title = Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody

The effectiveness of SARS-CoV-2 vaccines and therapeutic antibodies have been limited by the continuous emergence of viral variants and by the restricted diffusion of antibodies from circulation into the sites of respiratory virus infection. Here, we report the identification of two highly conserved regions on the Omicron variant receptor-binding domain recognized by broadly neutralizing antibodies. Furthermore, we generated a bispecific single-domain antibody that was able to simultaneously and synergistically bind these two regions on a single Omicron variant receptor-binding domain as revealed by cryo-EM structures. We demonstrated that this bispecific antibody can be effectively delivered to lung via inhalation administration and exhibits exquisite neutralization breadth and therapeutic efficacy in mouse models of SARS-CoV-2 infections. Importantly, this study also deciphered an uncommon and highly conserved cryptic epitope within the spike trimeric interface that may have implications for the design of broadly protective SARS-CoV-2 vaccines and therapeutics.

Therapeutic effects against SARS-CoV-2 infection are seen in mice after inhalation of an engineered, bispecific, single-domain antibody that simultaneously targets two points on the spike protein receptor-binding domain.

[end paper 4]

[begin paper 5]

PMCID = 11140111

Title = Single domain antibodies from camelids in the treatment of microbial infections

Infectious diseases continue to pose significant global health challenges. In addition to the enduring burdens of ailments like malaria and HIV, the emergence of nosocomial outbreaks driven by antibiotic-resistant pathogens underscores the ongoing threats. Furthermore, recent infectious disease crises, exemplified by the Ebola and SARS-CoV-2 outbreaks, have intensified the pursuit of more effective and efficient diagnostic and therapeutic solutions. Among the promising options, antibodies have garnered significant attention due to their favorable structural characteristics and versatile applications. Notably, nanobodies (Nbs), the smallest functional single-domain antibodies of heavy-chain only antibodies produced by camelids, exhibit remarkable capabilities in stable antigen binding. They offer unique advantages such as ease of expression and modification and enhanced stability, as well as improved hydrophilicity compared to conventional antibody fragments (antigen-binding fragments (Fab) or single-chain variable fragments (scFv)) that can aggregate due to their low solubility. Nanobodies directly target antigen epitopes or can be engineered into multivalent Nbs and Nb-fusion proteins, expanding their therapeutic potential. This review is dedicated to charting the progress in Nb research, particularly those derived from camelids, and highlighting their diverse applications in treating infectious diseases, spanning both human and animal contexts.

[end paper 5]

[begin paper 6]

PMCID = 9230756

Title = Single-Domain Antibodies as Therapeutics for Respiratory RNA Virus Infections

Over the years, infectious diseases with high morbidity and mortality disrupted human healthcare systems and devastated economies globally. Respiratory viruses, especially emerging or re-emerging RNA viruses, including influenza and human coronavirus, are the main pathogens of acute respiratory diseases that cause epidemics or even global pandemics. Importantly, due to the rapid mutation of viruses, there are few effective drugs and vaccines for the treatment and prevention of these RNA virus infections. Of note, a class of antibodies derived from camelid and shark, named nanobody or single-domain antibody (sdAb), was characterized by smaller size, lower production costs, more accessible binding epitopes, and inhalable properties, which have advantages in the treatment of respiratory diseases compared to conventional antibodies. Currently, a number of sdAbs have been developed against various respiratory RNA viruses and demonstrated potent therapeutic efficacy in mouse models. Here, we review the current status of the development of antiviral sdAb and discuss their potential as therapeutics for respiratory RNA viral diseases.

[end paper 6]

[begin paper 7]

PMCID = 8768012

Title = Bovine-derived antibodies and camelid-derived nanobodies as biotherapeutic weapons against SARS-CoV-2 and its variants: A review article

The Coronavirus Disease 2019 (COVID-19) pandemic, caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), has infected 305 million individuals worldwide and killed about 5.5 million people as of January 10, 2022. SARS-CoV-2 is the third major outbreak caused by a new coronavirus in the previous two decades, following SARS-CoV and MERS-CoV. Even though vaccination against SARS-CoV-2 is considered a critical strategy for preventing virus spread in the population and limiting COVID-19 clinical manifestations, new therapeutic drugs, and management strategies are urgently needed, particularly in light of the growing number of SARS-CoV-2 variants (such as Delta and Omicron variants). However, the use of conventional antibodies has faced many challenges, such as viral escape mutants, increased instability, weak binding, large sizes, the need for large amounts of plasma, and high-cost manufacturing. Furthermore, the emergence of new SARS-CoV-2 variants in the human population and recurrent coronavirus spillovers highlight the need for broadly neutralizing antibodies that are not affected by an antigenic drift that could limit future zoonotic infection. Bovine-derived antibodies and camelid-derived nanobodies are more potent and protective than conventional human antibodies, thanks to their inbuilt characteristics, and can be produced in large quantities. In addition, it was reported that these biotherapeutics are effective against a broad spectrum of epitopes, reducing the opportunity of viral pathogens to develop mutational escape. In this review, we focus on the potential benefits behind our rationale for using bovine-derived antibodies and camelid-derived nanobodies in countering SARS-CoV-2 and its emerging variants and mutants.

[end paper 7]

[begin paper 8]

PMCID = 8514607

Title = The role of single-domain antibodies (or nanobodies) in SARS-CoV-2 neutralization

The severe acute respiratory syndrome (SARS-CoV-2), a newly emerging of coronavirus, continues to infect humans in the absence of a viable treatment. Neutralizing antibodies that disrupt the interaction of RBD and ACE2 has been under the spotlight as a way of developing the COVID-19 treatment. Some animals, such as llamas, manufacture heavy-chain antibodies that have a single variable domain (VHH) instead of two variable domains (VH/VL) as opposed to typical antibodies. Nanobodies are antigen-specific, single-domain, changeable segments of camelid heavy chain-only antibodies that are recombinantly produced. These types of antibodies exhibit a wide range of strong physical and chemical properties, like high solubility, and stability. The VHH's high-affinity attachment to the receptor-binding domain (RBD) allowed the neutralization of SARS-CoV-2. To tackle COVID-19, some nanobodies are being developed against SARS-CoV-2, some of which have been recently included in clinical trials. Nanobody therapy may be useful in managing the COVID-19 pandemic as a potent and low-cost treatment. This paper describes the application of nanobodies as a new class of recombinant antibodies in COVID-19 treatment.

[end paper 8]

[begin paper 9]

PMCID = 10268213

Title = Fully synthetic platform to rapidly generate tetravalent bispecific nanobody–based immunoglobulins

Nanobodies are a promising class of biologics that can be used to prevent or treat viral infections. Here, we describe the production and validation of a discovery library that produces single-domain nanobodies using an engineered human antibody variable gene segment. As a test case, anti-SARS-CoV-2 nanobodies were isolated from this library and pairs of complementary nanobodies were incorporated into an antibody-like molecule that targets the receptor-binding domain using a biparatopic mode of engagement. This modular bispecific format enabled the rapid testing of nanobody pairs, and we show that incorporating pairs of nanobodies with different specificities can have synergistic effects on neutralization breadth and potency.

Nanobodies bind a target antigen with a kinetic profile similar to a conventional antibody, but exist as a single heavy chain domain that can be readily multimerized to engage antigen via multiple interactions. Presently, most nanobodies are produced by immunizing camelids; however, platforms for animal-free production are growing in popularity. Here, we describe the development of a fully synthetic nanobody library based on an engineered human VH3-23 variable gene and a multispecific antibody-like format designed for biparatopic target engagement. To validate our library, we selected nanobodies against the SARS-CoV-2 receptor–binding domain and employed an on-yeast epitope binning strategy to rapidly map the specificities of the selected nanobodies. We then generated antibody-like molecules by replacing the VH and VL domains of a conventional antibody with two different nanobodies, designed as a molecular clamp to engage the receptor-binding domain biparatopically. The resulting bispecific tetra-nanobody immunoglobulins neutralized diverse SARS-CoV-2 variants with potencies similar to antibodies isolated from convalescent donors. Subsequent biochemical analyses confirmed the accuracy of the on-yeast epitope binning and structures of both individual nanobodies, and a tetra-nanobody immunoglobulin revealed that the intended mode of interaction had been achieved. This overall workflow is applicable to nearly any protein target and provides a blueprint for a modular workflow for the development of multispecific molecules.

[end paper 9]

[begin paper 10]

PMCID = 8651292

Title = Highly synergistic combinations of nanobodies that target SARS-CoV-2 and are resistant to escape

The emergence of SARS-CoV-2 variants threatens current vaccines and therapeutic antibodies and urgently demands powerful new therapeutics that can resist viral escape. We therefore generated a large nanobody repertoire to saturate the distinct and highly conserved available epitope space of SARS-CoV-2 spike, including the S1 receptor binding domain, N-terminal domain, and the S2 subunit, to identify new nanobody binding sites that may reflect novel mechanisms of viral neutralization. Structural mapping and functional assays show that indeed these highly stable monovalent nanobodies potently inhibit SARS-CoV-2 infection, display numerous neutralization mechanisms, are effective against emerging variants of concern, and are resistant to mutational escape. Rational combinations of these nanobodies that bind to distinct sites within and between spike subunits exhibit extraordinary synergy and suggest multiple tailored therapeutic and prophylactic strategies.

[end paper 10]

[begin paper 11]

PMCID = 11076045

Title = Nanobody repertoire generated against the spike protein of ancestral SARS-CoV-2 remains efficacious against the rapidly evolving virus

To date, all major modes of monoclonal antibody therapy targeting SARS-CoV-2 have lost significant efficacy against the latest circulating variants. As SARS-CoV-2 omicron sublineages account for over 90% of COVID-19 infections, evasion of immune responses generated by vaccination or exposure to previous variants poses a significant challenge. A compelling new therapeutic strategy against SARS-CoV-2 is that of single-domain antibodies, termed nanobodies, which address certain limitations of monoclonal antibodies. Here, we demonstrate that our high-affinity nanobody repertoire, generated against wild-type SARS-CoV-2 spike protein (Mast et al., 2021), remains effective against variants of concern, including omicron BA.4/BA.5; a subset is predicted to counter resistance in emerging XBB and BQ.1.1 sublineages. Furthermore, we reveal the synergistic potential of nanobody cocktails in neutralizing emerging variants. Our study highlights the power of nanobody technology as a versatile therapeutic and diagnostic tool to combat rapidly evolving infectious diseases such as SARS-CoV-2.

[end paper 11]

[begin paper 12]

PMCID = 8001348

Title = Broad Reactivity Single Domain Antibodies against Influenza Virus and Their Applications to Vaccine Potency Testing and Immunotherapy

The antigenic variability of influenza presents many challenges to the development of vaccines and immunotherapeutics. However, it is apparent that there are epitopes on the virus that have evolved to remain largely constant due to their functional importance. These more conserved regions are often hidden and difficult to access by the human immune system but recent efforts have shown that these may be the Achilles heel of the virus through development and delivery of appropriate biological drugs. Amongst these, single domain antibodies (sdAbs) are equipped to target these vulnerabilities of the influenza virus due to their preference for concave epitopes on protein surfaces, their small size, flexible reformatting and high stability. Single domain antibodies are well placed to provide a new generation of robust analytical reagents and therapeutics to support the constant efforts to keep influenza in check.

[end paper 12]

[begin paper 13]

PMCID = 8956255

Title = Multivariate mining of an alpaca immune repertoire identifies potent cross-neutralizing SARS-CoV-2 nanobodies

Conventional approaches to isolate and characterize nanobodies are laborious. We combine phage display, multivariate enrichment, next-generation sequencing, and a streamlined screening strategy to identify numerous anti–severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) nanobodies. We characterize their potency and specificity using neutralization assays and hydrogen/deuterium exchange mass spectrometry (HDX-MS). The most potent nanobodies bind to the receptor binding motif of the receptor binding domain (RBD), and we identify two exceptionally potent members of this category (with monomeric half-maximal inhibitory concentrations around 13 and 16 ng/ml). Other nanobodies bind to a more conserved epitope on the side of the RBD and are able to potently neutralize the SARS-CoV-2 founder virus (42 ng/ml), the Beta variant (B.1.351/501Y.V2) (35 ng/ml), and also cross-neutralize the more distantly related SARS-CoV-1 (0.46 μg/ml). The approach presented here is well suited for the screening of phage libraries to identify functional nanobodies for various biomedical and biochemical applications.

High-throughput mining of camelid immune repertoires identified broad and potent nanobodies from an immunized alpaca.

[end paper 13]

[begin paper 14]

PMCID = 9100996

Title = Camelid Single-Domain Antibodies: Promises and Challenges as Lifesaving Treatments †

Since the discovery of camelid heavy-chain antibodies in 1993, there has been tremendous excitement for these antibody domains (VHHs/sdAbs/nanobodies) as research tools, diagnostics, and therapeutics. Commercially, several patents were granted to pioneering research groups in Belgium and the Netherlands between 1996–2001. Ablynx was established in 2001 with the aim of exploring the therapeutic applications and development of nanobody drugs. Extensive efforts over two decades at Ablynx led to the first approved nanobody drug, caplacizumab (Cablivi) by the EMA and FDA (2018–2019) for the treatment of rare blood clotting disorders in adults with acquired thrombotic thrombocytopenic purpura (TPP). The relatively long development time between camelid sdAb discovery and their entry into the market reflects the novelty of the approach, together with intellectual property restrictions and freedom-to-operate issues. The approval of the first sdAb drug, together with the expiration of key patents, may open a new horizon for the emergence of camelid sdAbs as mainstream biotherapeutics in the years to come. It remains to be seen if nanobody-based drugs will be cheaper than traditional antibodies. In this review, I provide critical perspectives on camelid sdAbs and present the promises and challenges to their widespread adoption as diagnostic and therapeutic agents.

[end paper 14]

[begin paper 15]

PMCID = 8951411

Title = Structural and Computational Studies of the SARS-CoV-2 Spike Protein Binding Mechanisms with Nanobodies: From Structure and Dynamics to Avidity-Driven Nanobody Engineering

Nanobodies provide important advantages over traditional antibodies, including their smaller size and robust biochemical properties such as high thermal stability, high solubility, and the ability to be bioengineered into novel multivalent, multi-specific, and high-affinity molecules, making them a class of emerging powerful therapies against SARS-CoV-2. Recent research efforts on the design, protein engineering, and structure-functional characterization of nanobodies and their binding with SARS-CoV-2 S proteins reflected a growing realization that nanobody combinations can exploit distinct binding epitopes and leverage the intrinsic plasticity of the conformational landscape for the SARS-CoV-2 S protein to produce efficient neutralizing and mutation resistant characteristics. Structural and computational studies have also been instrumental in quantifying the structure, dynamics, and energetics of the SARS-CoV-2 spike protein binding with nanobodies. In this review, a comprehensive analysis of the current structural, biophysical, and computational biology investigations of SARS-CoV-2 S proteins and their complexes with distinct classes of nanobodies targeting different binding sites is presented. The analysis of computational studies is supplemented by an in-depth examination of mutational scanning simulations and identification of binding energy hotspots for distinct nanobody classes. The review is focused on the analysis of mechanisms underlying synergistic binding of multivalent nanobodies that can be superior to single nanobodies and conventional nanobody cocktails in combating escape mutations by effectively leveraging binding avidity and allosteric cooperativity. We discuss how structural insights and protein engineering approaches together with computational biology tools can aid in the rational design of synergistic combinations that exhibit superior binding and neutralization characteristics owing to avidity-mediated mechanisms.

[end paper 15]

[begin paper 16]

PMCID = 9801699

Title = Applications of nanobodies in the prevention, detection, and treatment of the evolving SARS-CoV-2

Global health and economy are deeply influenced by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) and its newly emerging variants. Nanobodies with nanometer-scale size are promising for the detection and treatment of SARS-CoV-2 and its variants because they are superior to conventional antibodies in terms of cryptic epitope accessibility, tissue penetration, cost, formatting adaptability, and especially protein stability, which enables their aerosolized specific delivery to lung tissues. This review summarizes the progress in the prevention, detection, and treatment of SARS-CoV-2 using nanobodies, as well as strategies to combat the evolving SARS-CoV-2 variants. Generally, highly efficient generation of potent broad-spectrum nanobodies targeting conserved epitopes or further construction of multivalent formats targeting non-overlapping epitopes can promote neutralizing activity against SARS-CoV-2 variants and suppress immune escape.

[end paper 16]

[begin paper 17]

PMCID = 9792944

Title = Broadly neutralizing and protective nanobodies against SARS-CoV-2 Omicron subvariants BA.1, BA.2, and BA.4/5 and diverse sarbecoviruses

As SARS-CoV-2 Omicron and other variants of concern (VOCs) continue spreading worldwide, development of antibodies and vaccines to confer broad and protective activity is a global priority. Here, we report on the identification of a special group of nanobodies from immunized alpaca with potency against diverse VOCs including Omicron subvariants BA.1, BA.2 and BA.4/5, SARS-CoV-1, and major sarbecoviruses. Crystal structure analysis of one representative nanobody, 3-2A2-4, discovers a highly conserved epitope located between the cryptic and the outer face of the receptor binding domain (RBD), distinctive from the receptor ACE2 binding site. Cryo-EM and biochemical evaluation reveal that 3-2A2-4 interferes structural alteration of RBD required for ACE2 binding. Passive delivery of 3-2A2-4 protects K18-hACE2 mice from infection of authentic SARS-CoV-2 Delta and Omicron. Identification of these unique nanobodies will inform the development of next generation antibody therapies and design of pan-sarbecovirus vaccines.

The authors identify nanobodies from immunized alpaca with broadly neutralizing activity against SARS-CoV-1, SARS-CoV-2 variants, and major sarbecoviruses. One representative nanobody binds to a highly conserved epitope on RBD and protects K18-hACE2 mice from Omicron and Delta infection.

[end paper 17]

[begin paper 18]

PMCID = 10715488

Title = Identification of nurse shark VNAR single-domain antibodies targeting the spike S2 subunit of SARS-CoV-2

SARS-CoV-2 is the etiological agent of the COVID-19 pandemic. Antibody-based therapeutics targeting the spike protein, specifically the S1 subunit or the receptor binding domain (RBD) of SARS-CoV-2, have gained attention due to their clinical efficacy in treating patients diagnosed with COVID-19. An alternative to conventional antibody therapeutics is the use of shark new antigen variable receptor domain (VNAR) antibodies. VNARs are small (<15 kDa) and can reach deep into the pockets or grooves of the target antigen. Here, we have isolated 53 VNARs that bind to the S2 subunit by phage panning from a naïve nurse shark VNAR phage display library constructed in our laboratory. Among those binders, S2A9 showed the best neutralization activity against the original pseudotyped SARS-CoV-2 virus. Several binders, including S2A9, showed cross-reactivity against S2 subunits from other β coronaviruses. Furthermore, S2A9 showed neutralization activity against all variants of concern (VOCs) from alpha to omicron (including BA1, BA2, BA4, and BA5) in both pseudovirus and live virus neutralization assays. Our findings suggest that S2A9 could be a promising lead molecule for the development of broadly neutralizing antibodies against SARS-CoV-2 and emerging variants. The nurse shark VNAR phage library offers a novel platform that can be used to rapidly isolate single-domain antibodies against emerging viral pathogens.

[end paper 18]

[begin paper 19]

PMCID = 9219022

Title = Production and purification of shark and camel single domain antibodies from bacterial and mammalian cell expression systems

Single domain antibodies, including the antigen binding variable domains of the shark immunoglobulin new antigen receptor and the camelid variable region of the heavy chain, are the smallest antigen recognition domains (~15 kDa) and have unique characteristics compared to conventional antibodies. They are capable of binding epitopes that are hard to access for classical antibodies and can also be used for therapeutics or diagnostics, or modular building blocks for multi-domain constructs, antibody-drug conjugates, immunotoxins, or chimeric antigen receptor therapy. This protocol contains detailed procedures for the purification and validation of two single domain antibodies (one shark and one camel), which bind to the S2 subunit of the SARS-CoV-2 spike protein, using both bacterial and mammalian cell expression systems. It provides a comprehensive reference for the production of single domain antibodies with high yield, good quality, and purity.

[end paper 19]

[begin paper 20]

PMCID = 11368078

Title = Screening and affinity optimization of single domain antibody targeting the SARS-CoV-2 nucleocapsid protein

The coronavirus disease 2019 (COVID-19) pandemic, which caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), lead to a crisis with devastating disasters to global public economy and health. Several studies suggest that the SARS-CoV-2 nucleocapsid protein (N protein) is one of uppermost structural constituents of SARS-CoV-2 and is relatively conserved which could become a specific diagnostic marker. In this study, eight single domain antibodies recognized the N protein specifically which were named pN01–pN08 were screened using human phage display library. According to multiple sequence alignment and molecular docking analyses, the interaction mechanism between antibody and N protein was predicted. ELISA results indicated pN01–pN08 with high affinity to protein N. To improve their efficacy, two fusion proteins were prepared and their affinity was tested. These finding showed that fusion proteins had higher affinity than single domain antibodies and will be used as diagnosis for the pandemic of SARS-CoV-2.

[end paper 20]

[begin paper 21]

PMCID = 11148044

Title = Generation of nanobodies from transgenic ‘LamaMice’ lacking an endogenous immunoglobulin repertoire

Due to their exceptional solubility and stability, nanobodies have emerged as powerful building blocks for research tools and therapeutics. However, their generation in llamas is cumbersome and costly. Here, by inserting an engineered llama immunoglobulin heavy chain (IgH) locus into IgH-deficient mice, we generate a transgenic mouse line, which we refer to as ‘LamaMouse’. We demonstrate that LamaMice solely express llama IgH molecules without association to Igκ or λ light chains. Immunization of LamaMice with AAV8, the receptor-binding domain of the SARS-CoV-2 spike protein, IgE, IgG2c, and CLEC9A enabled us to readily select respective target-specific nanobodies using classical hybridoma and phage display technologies, single B cell screening, and direct cloning of the nanobody-repertoire into a mammalian expression vector. Our work shows that the LamaMouse represents a flexible and broadly applicable platform for a facilitated selection of target-specific nanobodies.

Nanobodies are normally made from immunized camelids, Ig transgenic mice or synthetic libraries. In this study, the authors introduce the llama Ig heavy chain locus into mice lacking this locus, thereby generating a line in which nanobodies can be made by direct immunization in the absence of an endogenous antibody repertoire.

[end paper 21]

[begin paper 22]

PMCID = 11460708

Title = Structure-guided in vitro evolution of nanobodies targeting new viral variants

A major challenge in antiviral antibody therapy is keeping up with the rapid evolution of viruses. Our research shows that nanobodies - single-domain antibodies derived from camelids - can be rapidly re-engineered to combat new viral strains through structure-guided in vitro evolution. Specifically, for viral mutations occurring at nanobody-binding sites, we introduce randomized amino acid sequences into nanobody residues near these mutations. We then select nanobody variants that effectively bind to the mutated viral target from a phage display library. As a proof of concept, we used this approach to adapt Nanosota-3, a nanobody originally identified to target the receptor-binding domain (RBD) of early Omicron subvariants, making it highly effective against recent Omicron subvariants. Remarkably, this adaptation process can be completed in less than two weeks, allowing drug development to keep pace with viral evolution and provide timely protection to humans.

The ongoing fight against viral diseases is made more difficult by the rapid evolution of viruses, which often outpaces current antiviral therapies. Our study addresses this critical issue by demonstrating the flexibility and rapid adaptability of antiviral nanobodies - single-domain antibodies derived from camelids. We have developed a structure-guided in vitro evolution strategy to quickly re-engineer nanobodies, enabling them to neutralize newly emerging viral variants. For viral mutations occurring at nanobody-binding sites, this approach introduces randomized amino acid sequences into nanobody residues near these mutations. Nanobody variants that effectively bind to the mutated viral target are then selected using a phage display library. Using this method, we successfully modified the nanobody Nanosota-3, originally an inhibitor of early Omicron subvariants, into a potent inhibitor of more recent Omicron subvariants. Remarkably, this adaptation process can be completed in under two weeks, significantly narrowing the gap between viral mutation rates and the development of effective therapeutic agents. Our findings have profound implications for antiviral drug development, particularly in light of ongoing global health challenges, providing a pathway to more timely and responsive treatments.

[end paper 22]

[begin paper 23]

PMCID = 9351521

Title = Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes

Understanding the structural principles that determine the binding affinity of nanobodies to the spike protein of severe acute respiratory syndrome coronavirus 2 has been difficult. We analyzed electron microscopy maps of nanobody-spike complexes and quantified the conformational entropy of binding. This informed the design of an engineered nanobody with improved binding to the spike protein. This result offers a guiding principle for the rational maturation of nanobodies directed against the spike. High-binding potency nanobodies have been shown to be effective in animal models; thus, this technology could have application in future pandemics.

Camelid single-domain antibodies, also known as nanobodies, can be readily isolated from naïve libraries for specific targets but often bind too weakly to their targets to be immediately useful. Laboratory-based genetic engineering methods to enhance their affinity, termed maturation, can deliver useful reagents for different areas of biology and potentially medicine. Using the receptor binding domain (RBD) of the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) spike protein and a naïve library, we generated closely related nanobodies with micromolar to nanomolar binding affinities. By analyzing the structure–activity relationship using X-ray crystallography, cryoelectron microscopy, and biophysical methods, we observed that higher conformational entropy losses in the formation of the spike protein–nanobody complex are associated with tighter binding. To investigate this, we generated structural ensembles of the different complexes from electron microscopy maps and correlated the conformational fluctuations with binding affinity. This insight guided the engineering of a nanobody with improved affinity for the spike protein.

[end paper 23]

[begin paper 24]

PMCID = 10865538

Title = Single-domain antibodies against SARS-CoV-2 RBD from a two-stage phage screening of universal and focused synthetic libraries

Coronavirus disease 2019 (COVID-19) is an evolving global pandemic, and nanobodies, as well as other single-domain antibodies (sdAbs), have been recognized as a potential diagnostic and therapeutic tool for infectious diseases. High-throughput screening techniques such as phage display have been developed as an alternative to in vivo immunization for the discovery of antibody-like target-specific binders.

We designed and constructed a highly diverse synthetic phage library sdAb-U (single-domain Antibody - Universal library ) based on a human framework. The SARS-CoV-2 receptor-binding domain (RBD) was expressed and purified. The universal library sdAb-U was panned against the RBD protein target for two rounds, followed by monoclonal phage ELISA (enzyme-linked immunosorbent assay) to identify RBD-specific binders (the first stage). High-affinity binders were sequenced and the obtained CDR1 and CDR2 sequences were combined with fully randomized CDR3 to construct a targeted (focused) phage library sdAb-RBD, for subsequent second-stage phage panning (also two rounds) and screening. Then, sequences with high single-to-background ratios in phage ELISA were selected for expression. The binding affinities of sdAbs to RBD were measured by an ELISA-based method. In addition, we conducted competition ELISA (using ACE2 ectodomain S19-D615) and SARS-CoV-2 pseudovirus neutralization assays for the high-affinity RBD-binding sdAb39.

Significant enrichments were observed in both the first-stage (universal library) and the second-stage (focused library) phage panning. Five RBD-specific binders were identified in the first stage with high ELISA signal-to-background ratios. In the second stage, we observed a much higher possibility of finding RBD-specific clones in phage ELISA. Among 45 selected RBD-positive sequences, we found eight sdAbs can be well expressed, and five of them show high-affinity to RBD (EC50 < 100nM). We finally found that sdAb39 (EC50 ~ 4nM) can compete with ACE2 for binding to RBD.

Overall, this two-stage strategy of synthetic phage display libraries enables rapid selection of SARS-CoV-2 RBD sdAb with potential therapeutic activity, and this two-stage strategy can potentially be used for rapid discovery of sdAbs against other targets.

The online version contains supplementary material available at 10.1186/s12879-024-09022-8.

[end paper 24]

[begin paper 25]

PMCID = 9170159

Title = Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants

Due to their small size, nanobodies can recognize protein cavities that are not accessible to conventional antibodies. In this report, we built dromedary camel (Camelus dromedarius) VHH phage libraries for the isolation of high-affinity nanobodies that broadly neutralize SARS-CoV-2 variants. Cryo-EM complex structures reveal that one dromedary camel VHH nanobody (8A2) binds the S1 subunit of the viral spike protein, and the other (7A3) targets a deeply buried region that uniquely extends to the S2 subunit beyond the S1 subunit. These nanobodies can protect mice from the lethal challenge of variants B.1.351 or B.1.617.2, suggesting the therapeutic potential of these nanobodies against COVID-19. The dromedary camel VHH libraries could be helpful to isolate neutralizing nanobodies against future emerging viruses quickly.

The severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) spike is a trimer of S1/S2 heterodimers with three receptor-binding domains (RBDs) at the S1 subunit for human angiotensin-converting enzyme 2 (hACE2). Due to their small size, nanobodies can recognize protein cavities that are not accessible to conventional antibodies. To isolate high-affinity nanobodies, large libraries with great diversity are highly desirable. Dromedary camels (Camelus dromedarius) are natural reservoirs of coronaviruses like Middle East respiratory syndrome CoV (MERS-CoV) that are transmitted to humans. Here, we built large dromedary camel VHH phage libraries to isolate nanobodies that broadly neutralize SARS-CoV-2 variants. We isolated two VHH nanobodies, NCI-CoV-7A3 (7A3) and NCI-CoV-8A2 (8A2), which have a high affinity for the RBD via targeting nonoverlapping epitopes and show broad neutralization activity against SARS-CoV-2 and its emerging variants of concern. Cryoelectron microscopy (cryo-EM) complex structures revealed that 8A2 binds the RBD in its up mode with a long CDR3 loop directly involved in the ACE2 binding residues and that 7A3 targets a deeply buried region that uniquely extends from the S1 subunit to the apex of the S2 subunit regardless of the conformational state of the RBD. At a dose of ≥5 mg/kg, 7A3 efficiently protected transgenic mice expressing hACE2 from the lethal challenge of variants B.1.351 or B.1.617.2, suggesting its therapeutic use against COVID-19 variants. The dromedary camel VHH phage libraries could be helpful as a unique platform ready for quickly isolating potent nanobodies against future emerging viruses.

[end paper 25]

[begin paper 26]

PMCID = 7857409

Title = An ultrapotent synthetic nanobody neutralizes SARS-CoV-2 by stabilizing inactive Spike

Monoclonal antibodies that bind to the spike protein of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) show therapeutic promise but must be produced in mammalian cells and need to be delivered intravenously. By contrast, single-domain antibodies called nanobodies can be produced in bacteria or yeast, and their stability may enable aerosol delivery. Two papers now report nanobodies that bind tightly to spike and efficiently neutralize SARS-CoV-2 in cells. Schoof et al. screened a yeast surface display of synthetic nanobodies and Xiang et al. screened anti-spike nanobodies produced by a llama. Both groups identified highly potent nanobodies that lock the spike protein in an inactive conformation. Multivalent constructs of selected nanobodies achieved even more potent neutralization.

Science, this issue p. 1473, p. 

Potent neutralizers of SARS-CoV-2 are identified by screening either synthetic or llama-produced nanobodies.

The severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) virus enters host cells via an interaction between its Spike protein and the host cell receptor angiotensin-converting enzyme 2 (ACE2). By screening a yeast surface-displayed library of synthetic nanobody sequences, we developed nanobodies that disrupt the interaction between Spike and ACE2. Cryo–electron microscopy (cryo-EM) revealed that one nanobody, Nb6, binds Spike in a fully inactive conformation with its receptor binding domains locked into their inaccessible down state, incapable of binding ACE2. Affinity maturation and structure-guided design of multivalency yielded a trivalent nanobody, mNb6-tri, with femtomolar affinity for Spike and picomolar neutralization of SARS-CoV-2 infection. mNb6-tri retains function after aerosolization, lyophilization, and heat treatment, which enables aerosol-mediated delivery of this potent neutralizer directly to the airway epithelia.

[end paper 26]

[begin paper 27]

PMCID = 11659936

Title = Single domain antibody: Development and application in biotechnology and biopharma

Heavy‐chain antibodies (HCAbs) are a unique type of antibodies devoid of light chains, and comprised of two heavy chains‐only that recognize their cognate antigen by virtue of a single variable domain also referred to as VHH, single domain antibody (sdAb), or nanobody (Nb). These functional HCAbs, serendipitous discovered about three decades ago, are exclusively found in camelids, comprising dromedaries, camels, llamas, and vicugnas. Nanobodies have become an essential tool in biomedical research and medicine, both in diagnostics and therapeutics due to their beneficial properties: small size, high stability, strong antigen‐binding affinity, low immunogenicity, low production cost, and straightforward engineering into more potent affinity reagents. The occurrence of HCAbs in camelids remains intriguing. It is believed to be an evolutionary adaptation, equipping camelids with a robust adaptive immune defense suitable to respond to the pressure from a pathogenic invasion necessitating a more profound antigen recognition and neutralization. This evolutionary innovation led to a simplified HCAb structure, possibly supported by genetic mutations and drift, allowing adaptive mutation and diversification in the heavy chain variable gene and constant gene regions. Beyond understanding their origins, the application of nanobodies has significantly advanced over the past 30 years. Alongside expanding laboratory research, there has been a rapid increase in patent application for nanobodies. The introduction of commercial nanobody drugs such as Cablivi, Nanozora, Envafolimab, and Carvykti has boosted confidence among in their potential. This review explores the evolutionary history of HCAbs, their ontogeny, and applications in biotechnology and pharmaceuticals, focusing on approved and ongoing medical research pipelines.

[end paper 27]

[begin paper 28]

PMCID = 9884143

Title = Expanding and improving nanobody repertoires using a yeast display method: Targeting SARS-CoV-2

COVID-19, caused by the coronavirus SARS-CoV-2, represents a serious worldwide health issue, with continually emerging new variants challenging current therapeutics. One promising alternate therapeutic avenue is represented by nanobodies, small single-chain antibodies derived from camelids with numerous advantageous properties and the potential to neutralize the virus. For identification and characterization of a broad spectrum of anti–SARS-CoV-2 Spike nanobodies, we further optimized a yeast display method, leveraging a previously published mass spectrometry-based method, using B-cell complementary DNA from the same immunized animals as a source of VHH sequences. Yeast display captured many of the sequences identified by the previous approach, as well as many additional sequences that proved to encode a large new repertoire of nanobodies with high affinities and neutralization activities against different SARS-CoV-2 variants. We evaluated DNA shuffling applied to the three complementarity-determining regions of antiviral nanobodies. The results suggested a surprising degree of modularity to complementarity-determining region function. Importantly, the yeast display approach applied to nanobody libraries from immunized animals allows parallel interrogation of a vast number of nanobodies. For example, we employed a modified yeast display to carry out massively parallel epitope binning. The current yeast display approach proved comparable in efficiency and specificity to the mass spectrometry–based approach, while requiring none of the infrastructure and expertise required for that approach, making these highly complementary approaches that together appear to comprehensively explore the paratope space. The larger repertoires produced maximize the likelihood of discovering broadly specific reagents and those that powerfully synergize in mixtures.

[end paper 28]

[begin paper 29]

PMCID = 11108896

Title = Nanobodies in the fight against infectious diseases: repurposing nature's tiny weapons

Nanobodies are the smallest known antigen-binding molecules to date. Their small size, good tissue penetration, high stability and solubility, ease of expression, refolding ability, and negligible immunogenicity in the human body have granted them excellence over conventional antibodies. Those exceptional attributes of nanobodies make them promising candidates for various applications in biotechnology, medicine, protein engineering, structural biology, food, and agriculture. This review presents an overview of their structure, development methods, advantages, possible challenges, and applications with special emphasis on infectious diseases-related ones. A showcase of how nanobodies can be harnessed for applications including neutralization of viruses and combating antibiotic-resistant bacteria is detailed. Overall, the impact of nanobodies in vaccine design, rapid diagnostics, and targeted therapies, besides exploring their role in deciphering microbial structures and virulence mechanisms are highlighted. Indeed, nanobodies are reshaping the future of infectious disease prevention and treatment.

[end paper 29]

[begin paper 30]

PMCID = 10968798

Title = Aptamers and Nanobodies as New Bioprobes for SARS-CoV-2 Diagnostic and Therapeutic System Applications

The global challenges posed by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) pandemic have underscored the critical importance of innovative and efficient control systems for addressing future pandemics. The most effective way to control the pandemic is to rapidly suppress the spread of the virus through early detection using a rapid, accurate, and easy-to-use diagnostic platform. In biosensors that use bioprobes, the binding affinity of molecular recognition elements (MREs) is the primary factor determining the dynamic range of the sensing platform. Furthermore, the sensitivity relies mainly on bioprobe quality with sufficient functionality. This comprehensive review investigates aptamers and nanobodies recently developed as advanced MREs for SARS-CoV-2 diagnostic and therapeutic applications. These bioprobes might be integrated into organic bioelectronic materials and devices, with promising enhanced sensitivity and specificity. This review offers valuable insights into advancing biosensing technologies for infectious disease diagnosis and treatment using aptamers and nanobodies as new bioprobes.

[end paper 30]

[begin paper 31]

PMCID = 10373554

Title = Broad Sarbecovirus Neutralizing Antibodies Obtained by Computational Design and Synthetic Library Screening

Members of the Sarbecovirus subgenus of Coronaviridae have twice caused deadly threats to humans. There is increasing concern about the rapid mutation of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), which has evolved into multiple generations of epidemic variants in 3 years. Broad neutralizing antibodies are of great importance for pandemic preparedness against SARS-CoV-2 variants and divergent zoonotic sarbecoviruses. Here, we analyzed the structural conservation of the receptor-binding domain (RBD) from representative sarbecoviruses and chose S2H97, a previously reported RBD antibody with ideal breadth and resistance to escape, as a template for computational design to enhance the neutralization activity and spectrum. A total of 35 designs were purified for evaluation. The neutralizing activity of a large proportion of these designs against multiple variants was increased from several to hundreds of times. Molecular dynamics simulation suggested that extra interface contacts and enhanced intermolecular interactions between the RBD and the designed antibodies are established. After light and heavy chain reconstitution, AI-1028, with five complementarity determining regions optimized, showed the best neutralizing activity across all tested sarbecoviruses, including SARS-CoV, multiple SARS-CoV-2 variants, and bat-derived viruses. AI-1028 recognized the same cryptic RBD epitope as the parental prototype antibody. In addition to computational design, chemically synthesized nanobody libraries are also a precious resource for rapid antibody development. By applying distinct RBDs as baits for reciprocal screening, we identified two novel nanobodies with broad activities. These findings provide potential pan-sarbecovirus neutralizing drugs and highlight new pathways to rapidly optimize therapeutic candidates when novel SARS-CoV-2 escape variants or new zoonotic coronaviruses emerge.

IMPORTANCE The subgenus Sarbecovirus includes human SARS-CoV, SARS-CoV-2, and hundreds of genetically related bat viruses. The continuous evolution of SARS-CoV-2 has led to the striking evasion of neutralizing antibody (NAb) drugs and convalescent plasma. Antibodies with broad activity across sarbecoviruses would be helpful to combat current SARS-CoV-2 mutations and longer term animal virus spillovers. The study of pan-sarbecovirus NAbs described here is significant for the following reasons. First, we established a structure-based computational pipeline to design and optimize NAbs to obtain more potent and broader neutralizing activity across multiple sarbecoviruses. Second, we screened and identified nanobodies from a highly diversified synthetic library with a broad neutralizing spectrum using an elaborate screening strategy. These methodologies provide guidance for the rapid development of antibody therapeutics against emerging pathogens with highly variable characteristics.

[end paper 31]

[begin paper 32]

PMCID = 8908544

Title = Structural basis of nanobodies neutralizing SARS-CoV-2 variants

Because of the evolutionary variants of SARS-CoV-2, development of broad-spectrum neutralizing antibodies resilient to virus escape is urgently needed. We identified a group of high-affinity nanobodies from camels immunized with receptor-binding domain (RBD) of SARS-CoV-2 spike protein and resolved the structures of two non-competing nanobodies (NB1A7 and NB1B11) in complex with RBD using X-ray crystallography. The structures show that NB1A7 targets the highly conserved cryptic epitope shared by SARS-CoV-2 variants and some other coronaviruses and blocks ACE2 receptor attachment of the spike protein, and NB1B11 epitope overlaps with the contacting surface of ACE2 and is different from the binding site of NB1A7. These two nanobodies were covalently linked into multivalent and bi-paratopic formats, which significantly improved the avidity and neutralization potency and may further inhibit viral escape. The results contribute to the structure-guided design of antibodies against future variants of SARS-CoV-2 virus to combat coronavirus epidemics and pandemics.

Shi et al. identify two neutralizing nanobodies against SARS-CoV-2. Crystal structures reveal how they prevent the virus and its variants from entering cells. The combination of two nanobodies significantly improves neutralization potency, which is a potential therapeutic candidate to reduce the probability of the emergence of escape variants of SARS-CoV-2.

[end paper 32]

[begin paper 33]

PMCID = 9043892

Title = Passive Immunotherapy Against SARS-CoV-2: From Plasma-Based Therapy to Single Potent Antibodies in the Race to Stay Ahead of the Variants

The COVID-19 pandemic is now approaching 2 years old, with more than 440 million people infected and nearly six million dead worldwide, making it the most significant pandemic since the 1918 influenza pandemic. The severity and significance of SARS-CoV-2 was recognized immediately upon discovery, leading to innumerable companies and institutes designing and generating vaccines and therapeutic antibodies literally as soon as recombinant SARS-CoV-2 spike protein sequence was available. Within months of the pandemic start, several antibodies had been generated, tested, and moved into clinical trials, including Eli Lilly’s bamlanivimab and etesevimab, Regeneron’s mixture of imdevimab and casirivimab, Vir’s sotrovimab, Celltrion’s regdanvimab, and Lilly’s bebtelovimab. These antibodies all have now received at least Emergency Use Authorizations (EUAs) and some have received full approval in select countries. To date, more than three dozen antibodies or antibody combinations have been forwarded into clinical trials. These antibodies to SARS-CoV-2 all target the receptor-binding domain (RBD), with some blocking the ability of the RBD to bind human ACE2, while others bind core regions of the RBD to modulate spike stability or ability to fuse to host cell membranes. While these antibodies were being discovered and developed, new variants of SARS-CoV-2 have cropped up in real time, altering the antibody landscape on a moving basis. Over the past year, the search has widened to find antibodies capable of neutralizing the wide array of variants that have arisen, including Alpha, Beta, Gamma, Delta, and Omicron. The recent rise and dominance of the Omicron family of variants, including the rather disparate BA.1 and BA.2 variants, demonstrate the need to continue to find new approaches to neutralize the rapidly evolving SARS-CoV-2 virus. This review highlights both convalescent plasma- and polyclonal antibody-based approaches as well as the top approximately 50 antibodies to SARS-CoV-2, their epitopes, their ability to bind to SARS-CoV-2 variants, and how they are delivered. New approaches to antibody constructs, including single domain antibodies, bispecific antibodies, IgA- and IgM-based antibodies, and modified ACE2-Fc fusion proteins, are also described. Finally, antibodies being developed for palliative care of COVID-19 disease, including the ramifications of cytokine release syndrome (CRS) and acute respiratory distress syndrome (ARDS), are described.

The online version contains supplementary material available at 10.1007/s40259-022-00529-7.

[end paper 33]

[begin paper 34]

PMCID = 11324105

Title = Structure defining of ultrapotent neutralizing nanobodies against MERS-CoV with novel epitopes on receptor binding domain

The Middle East Respiratory Syndrome Coronavirus (MERS-CoV) causes severe and fatal acute respiratory disease in humans. High fatality rates and continued infectiousness remain a pressing concern for global health preparedness. Antibodies targeted at the receptor-binding domain (RBD) are major countermeasures against human viral infection. Here, we report four potent nanobodies against MERS-CoV, which are isolated from alpaca, and especially the potency of Nb14 is highest in the pseudotyped virus assay. Structural studies show that Nb14 framework regions (FRs) are mainly involved in interactions targeting a novel epitope, which is entirely distinct from all previously reported antibodies, and disrupt the protein-carbohydrate interaction between residue W535 of RBD and hDPP4 N229-linked carbohydrate moiety (hDPP4-N229-glycan). Different from Nb14, Nb9 targets the cryptic face of RBD, which is distinctive from the hDPP4 binding site and the Nb14 epitope, and it induces the β5-β6 loop to inflect towards a shallow groove of the RBD and dampens the accommodation of a short helix of hDPP4. The particularly striking epitopes endow the two Nbs administrate synergistically in the pseudotyped MERS-CoV assays. These results not only character unprecedented epitopes for antibody recognition but also provide promising agents for prophylaxis and therapy of MERS-CoV infection.

MERS-CoV is one of the most prevalent zoonotic virus that has spread through 27 countries and infected more than 2,605 people since its first outbreak in Saudi Arabia in 2012. The high fatality rate and its persistent wide spread infectiousness in animal reservoirs have generated tremendous global public health concern. However, no licensed therapeutic agents or vaccines against MERS-CoV are currently available. To address the risk of MERS-CoV and its variants re-emergence, we developed four highly effective Nbs from alpaca and solved two crystal complexes of Nb9 and Nb14 with RBD. Remarkably, the neutralizing activity of Nb14 represents the highest of MERS-CoV antibodies reported to date. The novel epitopes of Nb14 and Nb9 locate outside the RBD and hDPP4 interface, and the unique different epitopes and mechanisms of Nb14 and Nb9 provide a better neutralizing for synergistically against MERS-CoV infection. Our findings provide insights into the cryptic epitopes on RBD and the development of antibodies against MERS-CoV infection.

[end paper 34]

[begin paper 35]

PMCID = 9850341

Title = The Potential of Nanobodies for COVID-19 Diagnostics and Therapeutics

The infectious severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) is the causative agent for coronavirus disease 2019 (COVID-19). Globally, there have been millions of infections and fatalities. Unfortunately, the virus has been persistent and a contributing factor is the emergence of several variants. The urgency to combat COVID-19 led to the identification/development of various diagnosis (polymerase chain reaction and antigen tests) and treatment (repurposed drugs, convalescent plasma, antibodies and vaccines) options. These treatments may treat mild symptoms and decrease the risk of life-threatening disease. Although these options have been fairly beneficial, there are some challenges and limitations, such as cost of tests/drugs, specificity, large treatment dosages, intravenous administration, need for trained personal, lengthy production time, high manufacturing costs, and limited availability. Therefore, the development of more efficient COVID-19 diagnostic and therapeutic options are vital. Nanobodies (Nbs) are novel monomeric antigen-binding fragments derived from camelid antibodies. Advantages of Nbs include low immunogenicity, high specificity, stability and affinity. These characteristics allow for rapid Nb generation, inexpensive large-scale production, effective storage, and transportation, which is essential during pandemics. Additionally, the potential aerosolization and inhalation delivery of Nbs allows for targeted treatment delivery as well as patient self-administration. Therefore, Nbs are a viable option to target SARS-CoV-2 and overcome COVID-19. In this review we discuss (1) COVID-19; (2) SARS-CoV-2; (3) the present conventional COVID-19 diagnostics and therapeutics, including their challenges and limitations; (4) advantages of Nbs; and (5) the numerous Nbs generated against SARS-CoV-2 as well as their diagnostic and therapeutic potential.

[end paper 35]

[begin paper 36]

PMCID = 9347709

Title = A Class of Shark‐Derived Single‐Domain Antibodies can Broadly Neutralize SARS‐Related Coronaviruses and the Structural Basis of Neutralization and Omicron Escape

The identification of a novel class of shark‐derived single domain antibodies, named vnarbodies that show picomolar affinities binding to the receptor binding domain (RBD) of Wuhan and Alpha, Beta, Kappa, Delta, Delta‐plus, and Lambda variants, is reported. Vnarbody 20G6 and 17F6 have broad neutralizing activities against all these SARS‐CoV‐2 viruses as well as other sarbecoviruses, including Pangolin coronavirus and Bat coronavirus. Intranasal administration of 20G6 effectively protects mice from the challenges of SARS‐CoV‐2 Wuhan and Beta variants. 20G6 and 17F6 contain a unique “WXGY” motif in the complementary determining region 3 that binds to a hidden epitope on RBD, which is highly conserved in sarbecoviruses through a novel β‐sheet interaction. It is found that the S375F mutation on Omicron RBD disrupts the structure of β‐strand, thus impair the binding with 20G6. The study demonstrates that shark‐derived vnarbodies offer a prophylactic and therapeutic option against most SARS‐CoV‐2 variants and provide insights into antibody evasion by the Omicron variant.

Shark‐derived vnarbodies 20G6 and 17F6 broadly neutralize SARS‐CoV‐2 Wuhan, Alpha, Beta, Kappa, Delta, Delta‐plus, Lambda variants, and sarbecovirus coronaviruses, but are unexpectedly ineffective for Omicron. Intranasal administration of 20G6 confers effective preventive and therapeutic effects in mice infected with SARS‐CoV‐2 Wuhan and Beta variant. Structural analysis elucidates the neutralizing mechanism and revealed the S375F mutation on Omicron receptor binding domain renders the evasion of neutralization by 20G6‐like antibodies.  

[end paper 36]

[begin paper 37]

PMCID = 10892724

Title = SARS-CoV-2 Specific Nanobodies Neutralize Different Variants of Concern and Reduce Virus Load in the Brain of h-ACE2 Transgenic Mice

Since the beginning of the COVID-19 pandemic, there has been a significant need to develop antivirals and vaccines to combat the disease. In this work, we developed llama-derived nanobodies (Nbs) directed against the receptor binding domain (RBD) and other domains of the Spike (S) protein of SARS-CoV-2. Most of the Nbs with neutralizing properties were directed to RBD and were able to block S-2P/ACE2 interaction. Three neutralizing Nbs recognized the N-terminal domain (NTD) of the S-2P protein. Intranasal administration of Nbs induced protection ranging from 40% to 80% after challenge with the WA1/2020 strain in k18-hACE2 transgenic mice. Interestingly, protection was associated with a significant reduction in virus replication in nasal turbinates and a reduction in virus load in the brain. Employing pseudovirus neutralization assays, we identified Nbs with neutralizing capacity against the Alpha, Beta, Delta, and Omicron variants, including a Nb capable of neutralizing all variants tested. Furthermore, cocktails of different Nbs performed better than individual Nbs at neutralizing two Omicron variants (B.1.529 and BA.2). Altogether, the data suggest the potential of SARS-CoV-2 specific Nbs for intranasal treatment of COVID-19 encephalitis.

[end paper 37]

[begin paper 38]

PMCID = 10688893

Title = Development of a bispecific nanobody conjugate broadly neutralizes diverse SARS-CoV-2 variants and structural basis for its broad neutralization

The continuous emergence of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) variants with increased transmissibility and profound immune-escape capacity makes it an urgent need to develop broad-spectrum therapeutics. Nanobodies have recently attracted extensive attentions due to their excellent biochemical and binding properties. Here, we report two high-affinity nanobodies (Nb-015 and Nb-021) that target non-overlapping epitopes in SARS-CoV-2 S-RBD. Both nanobodies could efficiently neutralize diverse viruses of SARS-CoV-2. The neutralizing mechanisms for the two nanobodies are further delineated by high-resolution nanobody/S-RBD complex structures. In addition, an Fc-based tetravalent nanobody format is constructed by combining Nb-015 and Nb-021. The resultant nanobody conjugate, designated as Nb-X2-Fc, exhibits significantly enhanced breadth and potency against all-tested SARS-CoV-2 variants, including Omicron sub-lineages. These data demonstrate that Nb-X2-Fc could serve as an effective drug candidate for the treatment of SARS-CoV-2 infection, deserving further in-vivo evaluations in the future.

The pandemic of SARS-CoV-2 has led to a severe public health crisis. In view of the wide clinical-applications of antibody drugs, it has always been a research focus to identify new antibodies and/or nanobodies with anti-viral neutralizing activity. In this study, we identified two neutralizing nanobodies (Nb-015 and Nb-021) that target non-overlapping epitopes in SARS-CoV-2 S-RBD with high affinity. Both nanobodies could broadly neutralize diverse SARS-CoV-2 variants. Furthermore, we revealed two distinct neutralization mechanisms of Nb-015 and Nb-021 by high-resolution nanobody/S-RBD complex structures. Eventually, we engineered a bispecific nanobody conjugate which exhibits excellent inhibitory activity against SARS-CoV-2, including the original strain and the VOI and VOC variants. We believe that the nanobody conjugate identified in this study could serve as an effective anti-viral drug reserve for potential treatment of COVID-19.

[end paper 38]

[begin paper 39]

PMCID = 11237593

Title = Human coronavirus OC43 nanobody neutralizes virus and protects mice from infection

Human coronavirus (hCoV) OC43 is endemic to global populations and usually causes asymptomatic or mild upper respiratory tract illness. Here, we demonstrate the neutralization efficacy of isolated nanobodies from alpacas immunized with the S1B and S1C domain of the hCoV-OC43 spike glycoprotein. A total of 40 nanobodies bound to recombinant OC43 protein with affinities ranging from 1 to 149 nM. Two nanobodies WNb 293 and WNb 294 neutralized virus at 0.21 and 1.79 nM, respectively. Intranasal and intraperitoneal delivery of WNb 293 fused to an Fc domain significantly reduced nasal viral load in a mouse model of hCoV-OC43 infection. Using X-ray crystallography, we observed that WNb 293 bound to an epitope on the OC43 S1B domain, distal from the sialoglycan-binding site involved in host cell entry. This result suggests that neutralization mechanism of this nanobody does not involve disruption of glycan binding. Our work provides characterization of nanobodies against hCoV-OC43 that blocks virus entry and reduces viral loads in vivo and may contribute to future nanobody-based therapies for hCoV-OC43 infections.

The pandemic potential presented by coronaviruses has been demonstrated by the ongoing COVID-19 pandemic and previous epidemics caused by severe acute respiratory syndrome coronavirus and Middle East respiratory syndrome coronavirus. Outside of these major pathogenic coronaviruses, there are four endemic coronaviruses that infect humans: hCoV-OC43, hCoV-229E, hCoV-HKU1, and hCoV-NL63. We identified a collection of nanobodies against human coronavirus OC43 (hCoV-OC43) and found that two high-affinity nanobodies potently neutralized hCoV-OC43 at low nanomolar concentrations. Prophylactic administration of one neutralizing nanobody reduced viral loads in mice infected with hCoV-OC43, showing the potential for nanobody-based therapies for hCoV-OC43 infections.

[end paper 39]

[begin paper 40]

PMCID = 8877688

Title = Allosteric Determinants of the SARS-CoV-2 Spike Protein Binding with Nanobodies: Examining Mechanisms of Mutational Escape and Sensitivity of the Omicron Variant

Structural and biochemical studies have recently revealed a range of rationally engineered nanobodies with efficient neutralizing capacity against the SARS-CoV-2 virus and resilience against mutational escape. In this study, we performed a comprehensive computational analysis of the SARS-CoV-2 spike trimer complexes with single nanobodies Nb6, VHH E, and complex with VHH E/VHH V nanobody combination. We combined coarse-grained and all-atom molecular simulations and collective dynamics analysis with binding free energy scanning, perturbation-response scanning, and network centrality analysis to examine mechanisms of nanobody-induced allosteric modulation and cooperativity in the SARS-CoV-2 spike trimer complexes with these nanobodies. By quantifying energetic and allosteric determinants of the SARS-CoV-2 spike protein binding with nanobodies, we also examined nanobody-induced modulation of escaping mutations and the effect of the Omicron variant on nanobody binding. The mutational scanning analysis supported the notion that E484A mutation can have a significant detrimental effect on nanobody binding and result in Omicron-induced escape from nanobody neutralization. Our findings showed that SARS-CoV-2 spike protein might exploit the plasticity of specific allosteric hotspots to generate escape mutants that alter response to binding without compromising activity. The network analysis supported these findings showing that VHH E/VHH V nanobody binding can induce long-range couplings between the cryptic binding epitope and ACE2-binding site through a broader ensemble of communication paths that is less dependent on specific mediating centers and therefore may be less sensitive to mutational perturbations of functional residues. The results suggest that binding affinity and long-range communications of the SARS-CoV-2 complexes with nanobodies can be determined by structurally stable regulatory centers and conformationally adaptable hotspots that are allosterically coupled and collectively control resilience to mutational escape.

[end paper 40]

[begin paper 41]

PMCID = 11111979

Title = Next generation single-domain antibodies against respiratory zoonotic RNA viruses

The global impact of zoonotic viral outbreaks underscores the pressing need for innovative antiviral strategies, particularly against respiratory zoonotic RNA viruses. These viruses possess a high potential to trigger future epidemics and pandemics due to their high mutation rate, broad host range and efficient spread through airborne transmission. Recent pandemics caused by coronaviruses and influenza A viruses underscore the importance of developing targeted antiviral strategies. Single-domain antibodies (sdAbs), originating from camelids, also known as nanobodies or VHHs (Variable Heavy domain of Heavy chain antibodies), have emerged as promising tools to combat current and impending zoonotic viral threats. Their unique structure, coupled with attributes like robustness, compact size, and cost-effectiveness, positions them as strong alternatives to traditional monoclonal antibodies. This review describes the pivotal role of sdAbs in combating respiratory zoonotic viruses, with a primary focus on enhancing sdAb antiviral potency through optimization techniques and diverse administration strategies. We discuss both the promises and challenges within this dynamically growing field.

[end paper 41]

[begin paper 42]

PMCID = 8420576

Title = Neutralization of SARS‐CoV‐2 by highly potent, hyperthermostable, and mutation‐tolerant nanobodies

Monoclonal anti‐SARS‐CoV‐2 immunoglobulins represent a treatment option for COVID‐19. However, their production in mammalian cells is not scalable to meet the global demand. Single‐domain (VHH) antibodies (also called nanobodies) provide an alternative suitable for microbial production. Using alpaca immune libraries against the receptor‐binding domain (RBD) of the SARS‐CoV‐2 Spike protein, we isolated 45 infection‐blocking VHH antibodies. These include nanobodies that can withstand 95°C. The most effective VHH antibody neutralizes SARS‐CoV‐2 at 17–50 pM concentration (0.2–0.7 µg per liter), binds the open and closed states of the Spike, and shows a tight RBD interaction in the X‐ray and cryo‐EM structures. The best VHH trimers neutralize even at 40 ng per liter. We constructed nanobody tandems and identified nanobody monomers that tolerate the K417N/T, E484K, N501Y, and L452R immune‐escape mutations found in the Alpha, Beta, Gamma, Epsilon, Iota, and Delta/Kappa lineages. We also demonstrate neutralization of the Beta strain at low‐picomolar VHH concentrations. We further discovered VHH antibodies that enforce native folding of the RBD in the E. coli cytosol, where its folding normally fails. Such “fold‐promoting” nanobodies may allow for simplified production of vaccines and their adaptation to viral escape‐mutations.

Single‐domain camelid antibodies that neutralize a range of common and emerging immune‐escape mutant strains of SARS‐CoV‐2 may constitute an easily‐producible option for treatment of COVID‐19 patients.  

[end paper 42]

[begin paper 43]

PMCID = 9834170

Title = Two pan-SARS-CoV-2 nanobodies and their multivalent derivatives effectively prevent Omicron infections in mice

With the widespread vaccinations against coronavirus disease 2019 (COVID-19), we are witnessing gradually waning neutralizing antibodies and increasing cases of breakthrough infections, necessitating the development of drugs aside from vaccines, particularly ones that can be administered outside of hospitals. Here, we present two cross-reactive nanobodies (R14 and S43) and their multivalent derivatives, including decameric ones (fused to the immunoglobulin M [IgM] Fc) that maintain potent neutralizing activity against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) after aerosolization and display not only pan-SARS-CoV-2 but also varied pan-sarbecovirus activities. Through respiratory administration to mice, monovalent and decameric R14 significantly reduce the lung viral RNAs at low dose and display potent pre- and post-exposure protection. Furthermore, structural studies reveal the neutralizing mechanisms of R14 and S43 and the multiple inhibition effects that the multivalent derivatives exert. Our work demonstrates promising convenient drug candidates via respiratory administration against SARS-CoV-2 infection, which can contribute to containing the COVID-19 pandemic.

Nanobodies R14 and S43 display not just pan-SARS-CoV-2 but varied pan-sarbecovirus activities

The multivalent nanobodies show enhanced neutralization, fitting the avidity effect

Intranasally administered MR14 potently prevents Omicron infections in mice

Structural studies reveal the neutralizing mechanisms of R14 and S43 as well as MR14

Liu et al. isolate two nanobodies (R14 and S43) and construct their multivalent derivatives with increased potencies and breadth against SARS-CoV-2 variants. Particularly, decameric R14, maintaining similar activities after aerosolization, efficiently prevents BA.2 infections in both pre- and post-exposure prophylactic settings in vivo and deserves further development.

[end paper 43]

[begin paper 44]

PMCID = 10444775

Title = Discovery and multimerization of cross-reactive single-domain antibodies against SARS-like viruses to enhance potency and address emerging SARS-CoV-2 variants

Coronaviruses have been the causative agent of three epidemics and pandemics in the past two decades, including the ongoing COVID-19 pandemic. A broadly-neutralizing coronavirus therapeutic is desirable not only to prevent and treat COVID-19, but also to provide protection for high-risk populations against future emergent coronaviruses. As all coronaviruses use spike proteins on the viral surface to enter the host cells, and these spike proteins share sequence and structural homology, we set out to discover cross-reactive biologic agents targeting the spike protein to block viral entry. Through llama immunization campaigns, we have identified single domain antibodies (VHHs) that are cross-reactive against multiple emergent coronaviruses (SARS-CoV, SARS-CoV-2, and MERS). Importantly, a number of these antibodies show sub-nanomolar potency towards all SARS-like viruses including emergent CoV-2 variants. We identified nine distinct epitopes on the spike protein targeted by these VHHs. Further, by engineering VHHs targeting distinct, conserved epitopes into multi-valent formats, we significantly enhanced their neutralization potencies compared to the corresponding VHH cocktails. We believe this approach is ideally suited to address both emerging SARS-CoV-2 variants during the current pandemic as well as potential future pandemics caused by SARS-like coronaviruses.

[end paper 44]

[begin paper 45]

PMCID = 10878242

Title = A novel strategy for an anti-idiotype vaccine: nanobody mimicking neutralization epitope of porcine circovirus type 2

Vaccination is the most effective method to protect humans and animals from diseases. Anti-idiotype vaccines are safer due to their absence of pathogens. However, the commercial production of traditional anti-idiotype vaccines using monoclonal and polyclonal antibodies (mAb and pAb) is complex and has a high failure rate. The present study designed a novel, simple, low-cost strategy for developing anti-idiotype vaccines with nanobody technology. We used porcine circovirus type 2 (PCV2) as a viral model, which can result in serious economic loss in the pig industry. The neutralizing mAb-1E7 (Ab1) against PCV2 capsid protein (PCV2-Cap) was immunized in the camel. And 12 nanobodies against mAb-1E7 were screened. Among them, Nb61 (Ab2) targeted the idiotype epitope of mAb-1E7 and blocked mAb-1E7’s binding to PCV2-Cap. Additionally, a high-dose Nb61 vaccination can also protect mice and pigs from PCV2 infection. Epitope mapping showed that mAb-1E7 recognized the 75NINDFL80 of PCV2-Cap and 101NYNDFLG107 of Nb61. Subsequently, the mAb-3G4 (Ab3) against Nb61 was produced and can neutralize PCV2 infection in the PK-15 cells. Structure analysis showed that the amino acids of mAb-1E7 and mAb-3G4 respective binding to PCV2-Cap and Nb61 were also similar on the amino acids sequences and spatial conformation. Collectively, our study first provided a strategy for producing nanobody-based anti-idiotype vaccines and identified that anti-idiotype nanobodies could mimic the antigen on amino acids and structures. Importantly, as more and more neutralization mAbs against different pathogens are prepared, anti-idiotype nanobody vaccines can be easily produced against the disease with our strategy, especially for dangerous pathogens.

Anti-idiotype vaccines utilize idiotype-anti-idiotype network theory, eliminating the need for external antigens as vaccine candidates. Especially for dangerous pathogens, they were safer because they did not contact the live pathogenic microorganisms. However, developing anti-idiotype vaccines with traditional monoclonal and polyclonal antibodies is complex and has a high failure rate. We present a novel, universal, simple, low-cost strategy for producing anti-idiotype vaccines with nanobody technology. Using a neutralization antibody against PCV2-Cap, a nanobody (Ab2) was successfully produced and could mimic the neutralizing epitope of PCV2-Cap. The nanobody can induce protective immune responses against PCV2 infection in mice and pigs. It highlighted that the anti-idiotype vaccine using nanobody has a very good application in the future, especially for dangerous pathogens.

[end paper 45]

[begin paper 46]

PMCID = 7199733

Title = Structural Basis for Potent Neutralization of Betacoronaviruses by Single-Domain Camelid Antibodies

Coronaviruses make use of a large envelope protein called spike (S) to engage host cell receptors and catalyze membrane fusion. Because of the vital role that these S proteins play, they represent a vulnerable target for the development of therapeutics. Here, we describe the isolation of single-domain antibodies (VHHs) from a llama immunized with prefusion-stabilized coronavirus spikes. These VHHs neutralize MERS-CoV or SARS-CoV-1 S pseudotyped viruses, respectively. Crystal structures of these VHHs bound to their respective viral targets reveal two distinct epitopes, but both VHHs interfere with receptor binding. We also show cross-reactivity between the SARS-CoV-1 S-directed VHH and SARS-CoV-2 S and demonstrate that this cross-reactive VHH neutralizes SARS-CoV-2 S pseudotyped viruses as a bivalent human IgG Fc-fusion. These data provide a molecular basis for the neutralization of pathogenic betacoronaviruses by VHHs and suggest that these molecules may serve as useful therapeutics during coronavirus outbreaks.

VHHs isolated from a llama immunized with prefusion-stabilized coronavirus spikes

Structural characterization of VHHs reveals conserved mechanism of neutralization

SARS-CoV-1 S-directed VHH cross-reacts with SARS-CoV-2 S

Bivalent VHH neutralizes SARS-CoV-2 pseudoviruses

Using llamas immunized with prefusion-stabilized betacoronavirus spike proteins, Wrapp et al. identify neutralizing cross-reactive single-domain camelid antibodies, which may serve not only as useful reagents for researchers studying the viruses causing MERS, SARS, and COVID-19, but also potential therapeutic candidates. Crystal structures further reveal how these antibodies bind spike proteins to prevent virus entry into cells.

[end paper 46]

[begin paper 47]

PMCID = 11407660

Title = Dual-role epitope on SARS-CoV-2 spike enhances and neutralizes viral entry across different variants

Grasping the roles of epitopes in viral glycoproteins is essential for unraveling the structure and function of these proteins. Up to now, all identified epitopes have been found to either neutralize, have no effect on, or enhance viral entry into cells. Here, we used nanobodies (single-domain antibodies) as probes to investigate a unique epitope on the SARS-CoV-2 spike protein, located outside the protein’s receptor-binding domain. Nanobody binding to this epitope enhances the cell entry of prototypic SARS-CoV-2, while neutralizing the cell entry of SARS-CoV-2 Omicron variant. Moreover, nanobody binding to this epitope promotes both receptor binding activity and post-attachment activity of prototypic spike, explaining the enhanced viral entry. The opposite occurs with Omicron spike, explaining the neutralized viral entry. This study reveals a unique epitope that can both enhance and neutralize viral entry across distinct viral variants, suggesting that epitopes may vary their roles depending on the viral context. Consequently, antibody therapies should be assessed across different viral variants to confirm their efficacy and safety.

Antibodies bind to specific epitopes on viral surface glycoproteins to perform their function: inhibiting viral infection, having no effect, or, in rare cases, enhancing viral infection. In our research, we used nanobodies (small, single-domain antibodies from camelid animals) as probes and identified a unique epitope on the SARS-CoV-2 spike protein with opposing functions across different SARS-CoV-2 variants. It enhances viral infection in pre-Omicron variants but inhibits it in the Omicron variant. We further investigated the molecular mechanism underlying these opposing effects. Although this epitope is not directly involved in receptor binding, nanobody binding to it modulates receptor binding and post-receptor-binding activities. This study marks the first discovery of a dual-function epitope on the SARS-CoV-2 spike protein that both enhances and inhibits viral infection across different viral variants. This discovery challenges the traditional categorization of epitopes, underscores the complex evolution of the SARS-CoV-2 spike protein, and offers new insights into antiviral antibody therapies.

[end paper 47]

[begin paper 48]

PMCID = 7857400

Title = Versatile and multivalent nanobodies efficiently neutralize SARS-CoV-2

Monoclonal antibodies that bind to the spike protein of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) show therapeutic promise but must be produced in mammalian cells and need to be delivered intravenously. By contrast, single-domain antibodies called nanobodies can be produced in bacteria or yeast, and their stability may enable aerosol delivery. Two papers now report nanobodies that bind tightly to spike and efficiently neutralize SARS-CoV-2 in cells. Schoof et al. screened a yeast surface display of synthetic nanobodies and Xiang et al. screened anti-spike nanobodies produced by a llama. Both groups identified highly potent nanobodies that lock the spike protein in an inactive conformation. Multivalent constructs of selected nanobodies achieved even more potent neutralization.

Science, this issue p. , p. 1479

Potent neutralizers of SARS-CoV-2 are identified by screening either synthetic or llama-produced nanobodies.

Cost-effective, efficacious therapeutics are urgently needed to combat the COVID-19 pandemic. In this study, we used camelid immunization and proteomics to identify a large repertoire of highly potent neutralizing nanobodies (Nbs) to the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) spike protein receptor binding domain (RBD). We discovered Nbs with picomolar to femtomolar affinities that inhibit viral infection at concentrations below the nanograms-per-milliliter level, and we determined a structure of one of the most potent Nbs in complex with the RBD. Structural proteomics and integrative modeling revealed multiple distinct and nonoverlapping epitopes and indicated an array of potential neutralization mechanisms. We bioengineered multivalent Nb constructs that achieved ultrahigh neutralization potency (half-maximal inhibitory concentration as low as 0.058 ng/ml) and may prevent mutational escape. These thermostable Nbs can be rapidly produced in bulk from microbes and resist lyophilization and aerosolization.

[end paper 48]

[begin paper 49]

PMCID = 9257560

Title = A panel of nanobodies recognizing conserved hidden clefts of all SARS-CoV-2 spike variants including Omicron

We are amid the historic coronavirus infectious disease 2019 (COVID-19) pandemic. Imbalances in the accessibility of vaccines, medicines, and diagnostics among countries, regions, and populations, and those in war crises, have been problematic. Nanobodies are small, stable, customizable, and inexpensive to produce. Herein, we present a panel of nanobodies that can detect the spike proteins of five SARS-CoV-2 variants of concern (VOCs) including Omicron. Here we show via ELISA, lateral flow, kinetic, flow cytometric, microscopy, and Western blotting assays that our nanobodies can quantify the spike variants. This panel of nanobodies broadly neutralizes viral infection caused by pseudotyped and authentic SARS-CoV-2 VOCs. Structural analyses show that the P86 clone targets epitopes that are conserved yet unclassified on the receptor-binding domain (RBD) and contacts the N-terminal domain (NTD). Human antibodies rarely access both regions; consequently, the clone buries hidden crevasses of SARS-CoV-2 spike proteins that go undetected by conventional antibodies.

A panel of nanobodies are presented that can detect the spike proteins of five SARS-CoV-2 variants of concern and structural analyses show that one clone targets conserved epitopes on the receptor-binding domain and contacts the N-terminal domain.

[end paper 49]

[begin paper 50]

PMCID = 8625641

Title = Structural Biology of Nanobodies against the Spike Protein of SARS-CoV-2

Nanobodies are 130 amino acid single-domain antibodies (VHH) derived from the unique heavy-chain-only subclass of Camelid immunogloblins. Their small molecular size, facile expression, high affinity and stability have combined to make them unique targeting reagents with numerous applications in the biomedical sciences. The first nanobody agent has now entered the clinic as a treatment against a blood disorder. The spread of the SARS-CoV-2 virus has seen the global scientific endeavour work to accelerate the development of technologies to try to defeat a pandemic that has now killed over four million people. In a remarkably short period of time, multiple studies have reported nanobodies directed against the viral Spike protein. Several agents have been tested in culture and demonstrate potent neutralisation of the virus or pseudovirus. A few agents have completed animal trials with very encouraging results showing their potential for treating infection. Here, we discuss the structural features that guide the nanobody recognition of the receptor binding domain of the Spike protein of SARS-CoV-2.

[end paper 50]

[begin paper 51]

PMCID = 11285730

Title = Structural and functional characterization of nanobodies that neutralize Omicron variants of SARS-CoV-2

The Omicron strains of SARS-CoV-2 pose a significant challenge to the development of effective antibody-based treatments as immune evasion has compromised most available immune therapeutics. Therefore, in the ‘arms race’ with the virus, there is a continuing need to identify new biologics for the prevention or treatment of SARS-CoV-2 infections. Here, we report the isolation of nanobodies that bind to the Omicron BA.1 spike protein by screening nanobody phage display libraries previously generated from llamas immunized with either the Wuhan or Beta spike proteins. The structure and binding properties of three of these nanobodies (A8, H6 and B5-5) have been characterized in detail providing insight into their binding epitopes on the Omicron spike protein. Trimeric versions of H6 and B5-5 neutralized the SARS-CoV-2 variant of concern BA.5 both in vitro and in the hamster model of COVID-19 following nasal administration. Thus, either alone or in combination could serve as starting points for the development of new anti-viral immunotherapeutics.

[end paper 51]

[begin paper 52]

PMCID = 8924699

Title = Recombinant Limosilactobacillus (Lactobacillus) delivering nanobodies against Clostridium perfringens NetB and alpha toxin confers potential protection from necrotic enteritis

Necrotic enteritis (NE), caused by Clostridium perfringens, is an intestinal disease with devastating economic losses to the poultry industry. NE is a complex disease and predisposing factors that compromise gut integrity are required to facilitate C. perfringens proliferation and toxin production. NE is also characterized by drastic shifts in gut microbiota; C. perfringens is negatively correlated with Lactobacilli. Vaccines are only partially effective against NE and antibiotics suffer from the concern of resistance development. These strategies address only some aspects of NE pathogenesis. Thus, there is an urgent need for alternative strategies that address multiple aspects of NE biology. Here, we developed Limosilactobacillus (Lactobacillus) reuteri vectors for in situ delivery of nanobodies against NetB and α toxin, two key toxins associated with NE pathophysiology. We generated nanobodies and showed that these nanobodies neutralize NetB and α toxin. We selected L. reuteri vector strains with intrinsic benefits and demonstrated that these strains inhibit C. perfringens and secrete over 130 metabolites, some of which play a key role in maintaining gut health. Recombinant L. reuteri strains efficiently secreted nanobodies and these nanobodies neutralized NetB. The recombinant strains were genetically and phenotypically stable over 480 generations and showed persistent colonization in chickens. A two‐dose in ovo and drinking water administration of recombinant L. reuteri strains protected chickens from NE‐associated mortality. These results provide proof‐of‐concept data for using L. reuteri as a live vector for delivery of nanobodies with broad applicability to other targets and highlight the potential synergistic effects of vector strains and nanobodies for addressing complex diseases such as NE.

Necrotic enteritis is one of the most common diseases of poultry with significant economic losses. Here, we show that Limosilactobacillus reuteri‐delivered single domain antibodies (nanobodies) protect chickens from this disease.  

[end paper 52]

[begin paper 53]

PMCID = 11554226

Title = Super broad and protective nanobodies against Sarbecoviruses including SARS-CoV-1 and the divergent SARS-CoV-2 subvariant KP.3.1.1

The ongoing evolution and immune escape of SARS-CoV-2, alongside the potential threat of SARS-CoV-1 and other sarbecoviruses, underscore the urgent need for effective strategies against their infection and transmission. This study highlights the discovery of nanobodies from immunized alpacas, which demonstrate exceptionally broad and potent neutralizing capabilities against the recently emerged and more divergent SARS-CoV-2 Omicron subvariants including JD.1.1, JN.1, KP.3, KP.3.1.1, as well as SARS-CoV-1 and coronaviruses from bats and pangolins utilizing receptor ACE2. Among these, Tnb04-1 emerges as the most broad and potent, binding to a conserved hydrophobic pocket in the spike’s receptor-binding domain, distinct from the ACE2 binding site. This interaction disrupts the formation of a proteinase K-resistant core, crucial for viral-cell fusion. Notably, intranasal administration of Tnb04-1 in Syrian hamsters effectively prevented respiratory infection and transmission of the authentic Omicron XBB.1.5 subvariant. Thus, Thb04-1 holds promise in combating respiratory acquisition and transmission of diverse sarbecoviruses.

As SARS-CoV-2 evolves and evades antibody immunity, new antibody intervention strategies are urgently needed to prevent viral acquisition and transmission. We identified a cluster of nanobodies from immunized alpacas with broad and potent neutralizing activity against all major SARS-CoV-2 variants, SARS-CoV-1, and ACE2-utilizing coronaviruses from bats and pangolins. Tnb04-1 was the most effective, binding to a conserved epitope in spike and providing strong protection against contact and respiratory infection of Omicron XBB.1.5 in Syrian hamsters. Tnb04-1 shows promise for next-generation antibody interventions against diverse sarbecoviruses.

[end paper 53]

[begin paper 54]

PMCID = 8021111

Title = Dromedary camels as a natural source of neutralizing nanobodies against SARS-CoV-2

The development of prophylactic and therapeutic agents for coronavirus disease 2019 (COVID-19) is a current global health priority. Here, we investigated the presence of cross-neutralizing antibodies against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in dromedary camels that were Middle East respiratory syndrome coronavirus (MERS-CoV) seropositive but MERS-CoV free. The tested 229 dromedaries had anti–MERS-CoV camel antibodies with variable cross-reactivity patterns against SARS-CoV-2 proteins, including the S trimer and M, N, and E proteins. Using SARS-CoV-2 competitive immunofluorescence immunoassays and pseudovirus neutralization assays, we found medium-to-high titers of cross-neutralizing antibodies against SARS-CoV-2 in these animals. Through linear B cell epitope mapping using phage immunoprecipitation sequencing and a SARS-CoV-2 peptide/proteome microarray, we identified a large repertoire of Betacoronavirus cross-reactive antibody specificities in these dromedaries and demonstrated that the SARS-CoV-2–specific VHH antibody repertoire is qualitatively diverse. This analysis revealed not only several SARS-CoV-2 epitopes that are highly immunogenic in humans, including a neutralizing epitope, but also epitopes exclusively targeted by camel antibodies. The identified SARS-CoV-2 cross-neutralizing camel antibodies are not proposed as a potential treatment for COVID-19. Rather, their presence in nonimmunized camels supports the development of SARS-CoV-2 hyperimmune camels, which could be a prominent source of therapeutic agents for the prevention and treatment of COVID-19.

[end paper 54]

[begin paper 55]

PMCID = 9356539

Title = Rapid and Quantitative In-vitro Evaluation of SARS-CoV-2 Neutralizing Antibodies and Nanobodies

Neutralizing monoclonal antibodies and nanobodies have shown promising results as potential therapeutic agents for COVID-19. Identifying such antibodies and nanobodies requires evaluating the neutralization activity of a large number of lead molecules via biological assays, such as the virus neutralization test (VNT). These assays are typically time-consuming and demanding on lab facilities. Here, we present a rapid and quantitative assay that evaluates the neutralizing efficacy of an antibody or nanobody within 1.5 hours, does not require BSL-2 facilities, and consumes only 8 μL of low concentration (ng/mL) sample for each assay run. We tested the human angiotensin-converting enzyme 2 (ACE2) binding inhibition efficacy of seven antibodies and eight nanobodies and verified that the IC50 values of our assay are comparable with those from SARS-CoV-2 pseudovirus neutralization tests. We also found that our assay could evaluate the neutralizing efficacy against three widespread SARS-CoV-2 variants. We observed increased affinity of these variants for ACE2, including the Beta and Gamma variants. Finally, we demonstrated that our assay enables rapid identification of an immune-evasive mutation of the SARS-CoV-2 spike protein utilizing a set of nanobodies with known binding epitopes.

[end paper 55]

[begin paper 56]

PMCID = 10167778

Title = Isolation and characterization of single domain antibodies from banded houndshark (Triakis scyllium) targeting SARS-CoV-2 spike RBD protein

The COVID-19 pandemic has significantly impacted human health for three years. To mitigate the spread of SARS-CoV-2, the development of neutralizing antibodies has been accelerated, including the exploration of alternative antibody formats such as single-domain antibodies. In this study, we identified variable new antigen receptors (VNARs) specific for the receptor binding domain (RBD) of SARS-CoV-2 by immunizing a banded houndshark (Triakis scyllium) with recombinant wild-type RBD. Notably, the CoV2NAR-1 clone showed high binding affinities in the nanomolar range to various RBDs and demonstrated neutralizing activity against SARS-CoV-2 pseudoviruses. These results highlight the potential of the banded houndshark as an animal model for the development of VNAR-based therapeutics or diagnostics against future pandemics.

[end paper 56]

[begin paper 57]

PMCID = 7642257

Title = Perspective: Reducing SARS-CoV2 Infectivity and Its Associated Immunopathology

COVID-19 has become difficult to contain in our interconnected world. In this article, we discuss some approaches that could reduce the consequences of COVID-19. We elaborate upon the utility of camelid single-domain antibodies (sdAbs), also referred to as nanobodies, which are naturally poised to neutralize viruses without enhancing its infectivity. Smaller sized sdAbs can be easily selected using microbes or the subcellular organelle display methods and can neutralize SARS-CoV2 infectivity. We also discuss issues related to their production using scalable platforms. The favorable outcome of the infection is evident in patients when the inflammatory response is adequately curtailed. Therefore, we discuss approaches to mitigate hyperinflammatory reactions initiated by SARS-CoV2 but orchestrated by immune mediators.

[end paper 57]

[begin paper 58]

PMCID = 9461429

Title = Arsenal of nanobodies shows broad-spectrum neutralization against SARS-CoV-2 variants of concern in vitro and in vivo in hamster models

Nanobodies offer several potential advantages over mAbs for the control of SARS-CoV-2. Their ability to access cryptic epitopes conserved across SARS-CoV-2 variants of concern (VoCs) and feasibility to engineer modular, multimeric designs, make these antibody fragments ideal candidates for developing broad-spectrum therapeutics against current and continually emerging SARS-CoV-2 VoCs. Here we describe a diverse collection of 37 anti-SARS-CoV-2 spike glycoprotein nanobodies extensively characterized as both monovalent and IgG Fc-fused bivalent modalities. The nanobodies were collectively shown to have high intrinsic affinity; high thermal, thermodynamic and aerosolization stability; broad subunit/domain specificity and cross-reactivity across existing VoCs; wide-ranging epitopic and mechanistic diversity and high and broad in vitro neutralization potencies. A select set of Fc-fused nanobodies showed high neutralization efficacies in hamster models of SARS-CoV-2 infection, reducing viral burden by up to six orders of magnitude to below detectable levels. In vivo protection was demonstrated with anti-RBD and previously unreported anti-NTD and anti-S2 nanobodies. This collection of nanobodies provides a potential therapeutic toolbox from which various cocktails or multi-paratopic formats could be built to combat multiple SARS-CoV-2 variants.

Isolation and extensive characterization of a collection of 37 anti-SARS-CoV-2 spike glycoprotein nanobodies show broad neutralization efficacies in vitro and in vivo in a hamster model of SARS-CoV-2 infection.

[end paper 58]

[begin paper 59]

PMCID = 8458290

Title = A potent SARS-CoV-2 neutralising nanobody shows therapeutic efficacy in the Syrian golden hamster model of COVID-19

SARS-CoV-2 remains a global threat to human health particularly as escape mutants emerge. There is an unmet need for effective treatments against COVID-19 for which neutralizing single domain antibodies (nanobodies) have significant potential. Their small size and stability mean that nanobodies are compatible with respiratory administration. We report four nanobodies (C5, H3, C1, F2) engineered as homotrimers with pmolar affinity for the receptor binding domain (RBD) of the SARS-CoV-2 spike protein. Crystal structures show C5 and H3 overlap the ACE2 epitope, whilst C1 and F2 bind to a different epitope. Cryo Electron Microscopy shows C5 binding results in an all down arrangement of the Spike protein. C1, H3 and C5 all neutralize the Victoria strain, and the highly transmissible Alpha (B.1.1.7 first identified in Kent, UK) strain and C1 also neutralizes the Beta (B.1.35, first identified in South Africa). Administration of C5-trimer via the respiratory route showed potent therapeutic efficacy in the Syrian hamster model of COVID-19 and separately, effective prophylaxis. The molecule was similarly potent by intraperitoneal injection.

Neutralizing nanobodies (Nb) are of considerable interest as therapeutic agents for COVID-19 treatment. Here, the authors functionally and structurally characterize Nbs that bind with high affinity to the receptor binding domain of the SARS-CoV-2 spike protein and show that an engineered homotrimeric Nb prevents disease progression in a Syrian hamster model of COVID-19 when administered intranasally.

[end paper 59]

[begin paper 60]

PMCID = 9482557

Title = Single domain antibodies derived from ancient animals as broadly neutralizing agents for SARS-CoV-2 and other coronaviruses

With severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) as an emergent human virus since December 2019, the world population is susceptible to coronavirus disease 2019 (COVID-19). SARS-CoV-2 has higher transmissibility than the previous coronaviruses, associated by the ribonucleic acid (RNA) virus nature with high mutation rate, caused SARS-CoV-2 variants to arise while circulating worldwide. Neutralizing antibodies are identified as immediate and direct-acting therapeutic against COVID-19. Single-domain antibodies (sdAbs), as small biomolecules with non-complex structure and intrinsic stability, can acquire antigen-binding capabilities comparable to conventional antibodies, which serve as an attractive neutralizing solution. SARS-CoV-2 spike protein attaches to human angiotensin-converting enzyme 2 (ACE2) receptor on lung epithelial cells to initiate viral infection, serves as potential therapeutic target. sdAbs have shown broad neutralization towards SARS-CoV-2 with various mutations, effectively stop and prevent infection while efficiently block mutational escape. In addition, sdAbs can be developed into multivalent antibodies or inhaled biotherapeutics against COVID-19.

.

[end paper 60]

[begin paper 61]

PMCID = 7112682

Title = Use of camel single-domain antibodies for the diagnosis and treatment of zoonotic diseases

VHHs provide many advantages over complete IgG in diagnostics and therapy.

Toxins and viruses are more efficiently neutralized by multivalent VHHs.

Camelids could be a source of broadly neutralizing antibodies (bNAbs) to treat zoonotic diseases.

Camelids produce both conventional heterotetrameric antibodies and homodimeric heavy-chain only antibodies. The antigen-binding region of such homodimeric heavy-chain only antibodies consists of one single domain, called VHH. VHHs provide many advantages over conventional full-sized antibodies and currently used antibody-based fragments (Fab, scFv), including high specificity, stability and solubility, and small size, allowing them to recognize unusual antigenic sites and deeply penetrate tissues. Since their discovery, VHHs have been used extensively in diagnostics and therapy. In recent decades, the number of outbreaks of diseases transmissible from animals to humans has been on the rise. In this review, we evaluate the status of VHHs as diagnostic and therapeutic biomolecular agents for the detection and treatment of zoonotic diseases, such as bacterial, parasitic, and viral zoonosis. VHHs show great adaptability to inhibit or neutralize pathogenic agents for the creation of multifunctional VHH-based diagnostic and therapeutic molecules against zoonotic diseases.

[end paper 61]

[begin paper 62]

PMCID = 11211474

Title = A broad neutralizing nanobody against SARS-CoV-2 engineered from an approved drug

SARS-CoV-2 infection is initiated by Spike glycoprotein binding to the human angiotensin-converting enzyme 2 (ACE2) receptor via its receptor binding domain. Blocking this interaction has been proven to be an effective approach to inhibit virus infection. Here we report the discovery of a neutralizing nanobody named VHH60, which was directly produced from an engineering nanobody library based on a commercialized nanobody within a very short period. VHH60 competes with human ACE2 to bind the receptor binding domain of the Spike protein at S351, S470-471and S493-494 as determined by structural analysis, with an affinity of 2.56 nM. It inhibits infections of both ancestral SARS-CoV-2 strain and pseudotyped viruses harboring SARS-CoV-2 wildtype, key mutations or variants at the nanomolar level. Furthermore, VHH60 suppressed SARS-CoV-2 infection and propagation 50-fold better and protected mice from death for twice as long as the control group after SARS-CoV-2 nasal infections in vivo. Therefore, VHH60 is not only a powerful nanobody with a promising profile for disease control but also provides evidence for a highly effective and rapid approach to generating therapeutic nanobodies.

[end paper 62]

[begin paper 63]

PMCID = 9150821

Title = Anti-HIV-1 Nanobody-IgG1 Constructs With Improved Neutralization Potency and the Ability to Mediate Fc Effector Functions

The most effective treatment for HIV-1, antiretroviral therapy, suppresses viral replication and averts the disease from progression. Nonetheless, there is a need for alternative treatments as it requires daily administration with the possibility of side effects and occurrence of drug resistance. Broadly neutralizing antibodies or nanobodies targeting the HIV-1 envelope glycoprotein are explored as alternative treatment, since they mediate viral suppression and contribute to the elimination of virus-infected cells. Besides neutralization potency and breadth, Fc-mediated effector functions of bNAbs also contribute to the in vivo efficacy. In this study multivalent J3, 2E7 and 1F10 anti-HIV-1 broadly neutralizing nanobodies were generated to improve neutralization potency and IgG1 Fc fusion was utilized to gain Fc-mediated effector functions. Bivalent and trivalent nanobodies, coupled using long glycine-serine linkers, showed increased binding to the HIV-1 Env and enhanced neutralization potency compared to the monovalent variant. Fusion of an IgG1 Fc domain to J3 improved neutralization potency compared to the J3-bihead and restored Fc-mediated effector functions such as antibody-dependent cellular phagocytosis and trogocytosis, and natural killer cell activation. Due to their neutralization breadth and potency and their ability to induce effector functions these nanobody-IgG1 constructs may prove to be valuable towards alternative HIV-1 therapies.

[end paper 63]

[begin paper 64]

PMCID = 10955499

Title = Plant virus‐derived nanoparticles decorated with genetically encoded SARS‐CoV‐2 nanobodies display enhanced neutralizing activity

Viral nanoparticles (VNPs) are a new class of virus‐based formulations that can be used as building blocks to implement a variety of functions of potential interest in biotechnology and nanomedicine. Viral coat proteins (CP) that exhibit self‐assembly properties are particularly appropriate for displaying antigens and antibodies, by generating multivalent VNPs with therapeutic and diagnostic potential. Here, we developed genetically encoded multivalent VNPs derived from two filamentous plant viruses, potato virus X (PVX) and tobacco etch virus (TEV), which were efficiently and inexpensively produced in the biofactory Nicotiana benthamiana plant. PVX and TEV‐derived VNPs were decorated with two different nanobodies recognizing two different regions of the receptor‐binding domain (RBD) of the SARS‐CoV‐2 Spike protein. The addition of different picornavirus 2A ribosomal skipping peptides between the nanobody and the CP allowed for modulating the degree of VNP decoration. Nanobody‐decorated VNPs purified from N. benthamiana tissues successfully recognized the RBD antigen in enzyme‐linked immunosorbent assays and showed efficient neutralization activity against pseudoviruses carrying the Spike protein. Interestingly, multivalent PVX and TEV‐derived VNPs exhibited a neutralizing activity approximately one order of magnitude higher than the corresponding nanobody in a dimeric format. These properties, combined with the ability to produce VNP cocktails in the same N. benthamiana plant based on synergistic infection of the parent PVX and TEV, make these green nanomaterials an attractive alternative to standard antibodies for multiple applications in diagnosis and therapeutics.

[end paper 64]

[begin paper 65]

PMCID = 9411660

Title = Research progress and applications of nanobody in human infectious diseases

Infectious diseases, caused by pathogenic microorganisms, are capable of affecting crises. In addition to persistent infectious diseases such as malaria and dengue fever, the vicious outbreaks of infectious diseases such as Neocon, Ebola and SARS-CoV-2 in recent years have prompted the search for more efficient and convenient means for better diagnosis and treatment. Antibodies have attracted a lot of attention due to their good structural characteristics and applications. Nanobodies are the smallest functional single-domain antibodies known to be able to bind stably to antigens, with the advantages of high stability, high hydrophilicity, and easy expression and modification. They can directly target antigen epitopes or be constructed as multivalent nanobodies or nanobody fusion proteins to exert therapeutic effects. This paper focuses on the construction methods and potential functions of nanobodies, outlines the progress of their research, and highlights their various applications in human infectious diseases.

[end paper 65]

[begin paper 66]

PMCID = 10590698

Title = Nanobodies with cross-neutralizing activity provide prominent therapeutic efficacy in mild and severe COVID-19 rodent models

The weakened protective efficacy of COVID-19 vaccines and antibodies caused by SARS-CoV-2 variants presents a global health emergency, which underscores the urgent need for universal therapeutic antibody intervention for clinical patients. Here, we screened three alpacas-derived nanobodies (Nbs) with neutralizing activity from twenty RBD-specific Nbs. The three Nbs were fused with the Fc domain of human IgG, namely aVHH-11-Fc, aVHH-13-Fc and aVHH-14-Fc, which could specifically bind RBD protein and competitively inhibit the binding of ACE2 receptor to RBD. They effectively neutralized SARS-CoV-2 pseudoviruses D614G, Alpha, Beta, Gamma, Delta, and Omicron sub-lineages BA.1, BA.2, BA.4, and BA.5 and authentic SARS-CoV-2 prototype, Delta, and Omicron BA.1, BA.2 strains. In mice-adapted COVID-19 severe model, intranasal administration of aVHH-11-Fc, aVHH-13-Fc and aVHH-14-Fc effectively protected mice from lethal challenges and reduced viral loads in both the upper and lower respiratory tracts. In the COVID-19 mild model, aVHH-13-Fc, which represents the optimal neutralizing activity among the above three Nbs, effectively protected hamsters from the challenge of SARS-CoV-2 prototype, Delta, Omicron BA.1 and BA.2 by significantly reducing viral replication and pathological alterations in the lungs. In structural modeling of aVHH-13 and RBD, aVHH-13 binds to the receptor-binding motif region of RBD and interacts with some highly conserved epitopes. Taken together, our study illustrated that alpaca-derived Nbs offered a therapeutic countermeasure against SARS-CoV-2, including those Delta and Omicron variants which have evolved into global pandemic strains.

Alpaca-derived nanobodies showed a cross-neutralizing activity against SARS-CoV-2 variants.

aVHH-13-Fc provided complete protection in mild and severe COVID-19 rodent models.

The binding site between aVHH-13-Fc and the RBD variant of SARS-CoV-2 is partially located on the RBM.

[end paper 66]

[begin paper 67]

PMCID = 8333356

Title = Potent neutralizing nanobodies resist convergent circulating variants of SARS-CoV-2 by targeting diverse and conserved epitopes

Interventions against variants of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) are urgently needed. Stable and potent nanobodies (Nbs) that target the receptor binding domain (RBD) of SARS-CoV-2 spike are promising therapeutics. However, it is unknown if Nbs broadly neutralize circulating variants. We found that RBD Nbs are highly resistant to variants of concern (VOCs). High-resolution cryoelectron microscopy determination of eight Nb-bound structures reveals multiple potent neutralizing epitopes clustered into three classes: Class I targets ACE2-binding sites and disrupts host receptor binding. Class II binds highly conserved epitopes and retains activity against VOCs and RBDSARS-CoV. Cass III recognizes unique epitopes that are likely inaccessible to antibodies. Systematic comparisons of neutralizing antibodies and Nbs provided insights into how Nbs target the spike to achieve high-affinity and broadly neutralizing activity. Structure-function analysis of Nbs indicates a variety of antiviral mechanisms. Our study may guide the rational design of pan-coronavirus vaccines and therapeutics.

Highly potent neutralizing nanobodies (Nbs) are of great interest as potential COVID-19 therapeutics. Here, the authors show that potent neutralizing Nbs targeting the receptor binding domain (RBD) of the SARS-CoV-2 spike protein are also effective against convergent variants of concern of the virus. They determine eight Nb-bound spike protein cryo-EM structures, classify the binding epitopes of the Nbs and discuss their neutralization mechanisms.

[end paper 67]

[begin paper 68]

PMCID = 10833066

Title = NanoLAS: a comprehensive nanobody database with data integration, consolidation and application

Nanobodies, a unique subclass of antibodies first discovered in camelid animals, are composed solely of a single heavy chain’s variable region. Their significantly reduced molecular weight, in comparison to conventional antibodies, confers numerous advantages in the treatment of various diseases. As research and applications involving nanobodies expand, the quantity of identified nanobodies is also rapidly growing. However, the existing antibody databases are deficient in type and coverage, failing to satisfy the comprehensive needs of researchers and thus impeding progress in nanobody research.

In response to this, we have amalgamated data from multiple sources to successfully assemble a new and comprehensive nanobody database. This database has currently included the latest nanobody data and provides researchers with an excellent search and data display interface, thus facilitating the progression of nanobody research and their application in disease treatment.

In summary, the newly constructed Nanobody Library and Archive System may significantly enhance the retrieval efficiency and application potential of nanobodies. We envision that Nanobody Library and Archive System will serve as an accessible, robust and efficient tool for nanobody research and development, propelling advancements in the field of biomedicine.

 Database URL: https://www.nanolas.cloud

[end paper 68]

[begin paper 69]

PMCID = 11515141

Title = Discovery of nanobodies: a comprehensive review of their applications and potential over the past five years

Nanobodies (Nbs) are antibody fragments derived from heavy-chain-only IgG antibodies found in the Camelidae family as well as cartilaginous fish. Their unique structural and functional properties, such as their small size, the ability to be engineered for high antigen-binding affinity, stability under extreme conditions, and ease of production, have made them promising tools for diagnostics and therapeutics. This potential was realized in 2018 with the approval of caplacizumab, the world’s first Nb-based drug. Currently, Nbs are being investigated in clinical trials for a broad range of treatments, including targeted therapies against PDL1 and Epidermal Growth Factor Receptor (EGFR), cardiovascular diseases, inflammatory conditions, and neurodegenerative disorders such as Alzheimer’s disease, Parkinson’s disease, and amyotrophic lateral sclerosis. They are also being studied for their potential for detecting and imaging autoimmune conditions and infectious diseases such as severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). A variety of methods are now available to generate target-specific Nbs quickly and efficiently at low costs, increasing their accessibility. This article examines these diverse applications of Nbs and their promising roles. Only the most recent articles published in the last five years have been used to summarize the most advanced developments in the field.

[end paper 69]

[begin paper 70]

PMCID = 11054741

Title = Engineered Multivalent Nanobodies Efficiently Neutralize SARS-CoV-2 Omicron Subvariants BA.1, BA.4/5, XBB.1 and BQ.1.1

Most available neutralizing antibodies are ineffective against highly mutated SARS-CoV-2 Omicron subvariants. Therefore, it is crucial to develop potent and broad-spectrum alternatives to effectively manage Omicron subvariants. Here, we constructed a high-diversity nanobody phage display library and identified nine nanobodies specific to the SARS-CoV-2 receptor-binding domain (RBD). Five of them exhibited cross-neutralization activity against the SARS-CoV-2 wild-type (WT) strain and the Omicron subvariants BA.1 and BA.4/5, and one nanobody demonstrated marked efficacy even against the Omicron subvariants BQ.1.1 and XBB.1. To enhance the therapeutic potential, we engineered a panel of multivalent nanobodies with increased neutralizing potency and breadth. The most potent multivalent nanobody, B13-B13-B13, cross-neutralized all tested pseudoviruses, with a geometric mean of the 50% inhibitory concentration (GM IC50) value of 20.83 ng/mL. An analysis of the mechanism underlying the enhancement of neutralization breadth by representative multivalent nanobodies demonstrated that the strategic engineering approach of combining two or three nanobodies into a multivalent molecule could improve the affinity between a single nanobody and spike, and could enhance tolerance toward escape mutations such as R346T and N460K. Our engineered multivalent nanobodies may be promising drug candidates for treating and preventing infection with Omicron subvariants and even future variants.

[end paper 70]

[begin paper 71]

PMCID = 8699001

Title = Central Nervous System Delivery of Antibodies and Their Single-Domain Antibodies and Variable Fragment Derivatives with Focus on Intranasal Nose to Brain Administration

IgG antibodies are some of the most important biopharmaceutical molecules with a high market volume. In spite of the fact that clinical therapies with antibodies are broadly utilized in oncology, immunology and hematology, their delivery strategies and biodistribution need improvement, their limitations being due to their size and poor ability to penetrate into tissues. In view of their small size, there is a rising interest in derivatives, such as single-domain antibodies and single-chain variable fragments, for clinical diagnostic but also therapeutic applications. Smaller antibody formats combine several benefits for clinical applications and can be manufactured at reduced production costs compared with full-length IgGs. Moreover, such formats have a relevant potential for targeted drug delivery that directs drug cargo to a specific tissue or across the blood–brain barrier. In this review, we give an overview of the challenges for antibody drug delivery in general and focus on intranasal delivery to the central nervous system with antibody formats of different sizes.

[end paper 71]

[begin paper 72]

PMCID = 11347438

Title = A single domain antibody-based Luminex assay for the detection of SARS-CoV-2 in clinical samples

Within the past decade, single domain antibodies (sdAbs) have been recognized as unique affinity binding reagents that can be tailored for performance in a variety of immunoassay formats. Luminex MagPlex color-coded magnetic microspheres provide a high-throughput platform that enables multiplexed immunoassays. We developed a MagPlex bead-based assay for the detection of SARS-CoV-2, using sdAbs against SARS-CoV-2 nucleocapsid (N) protein in which we engineered the sdAb capture reagents to orient them on the beads. The oriented sdAbs provided an increase in sensitivity over randomly oriented sdAbs for samples of N diluted in buffer, which also translated into better detection of SARS-CoV-2 in clinical samples. We assessed the specificity of the assay by examining seasonal coronavirus clinical samples. In summary, we provide a proof-of-concept that a bead-based assay using sdAbs to detect SARS-CoV-2 is feasible and future research combining it with other sdAb-coated beads that can detect other viruses may provide a useful diagnostic tool.

[end paper 72]

[begin paper 73]

PMCID = 6640686

Title = Single-Domain Antibodies and Their Formatting to Combat Viral Infections

Since their discovery in the 1990s, single-domain antibodies (VHHs), also known as Nanobodies®, have changed the landscape of affinity reagents. The outstanding solubility, stability, and specificity of VHHs, as well as their small size, ease of production and formatting flexibility favor VHHs over conventional antibody formats for many applications. The exceptional ease by which it is possible to fuse VHHs with different molecular modules has been particularly explored in the context of viral infections. In this review, we focus on VHH formats that have been developed to combat viruses including influenza viruses, human immunodeficiency virus-1 (HIV-1), and human respiratory syncytial virus (RSV). Such formats may significantly increase the affinity, half-life, breadth of protection of an antiviral VHH and reduce the risk of viral escape. In addition, VHHs can be equipped with effector functions, for example to guide components of the immune system with high precision to sites of viral infection.

[end paper 73]

[begin paper 74]

PMCID = 11609455

Title = Nanobodies: From High-Throughput Identification to Therapeutic Development

The camelid single-domain antibody fragment, commonly referred to as a nanobody, achieves the targeting power of conventional monoclonal antibodies (mAbs) at only a fraction of their size. Isolated from camelid species (including llamas, alpacas, and camels), their small size at ∼15 kDa, low structural complexity, and high stability compared with conventional antibodies have propelled nanobody technology into the limelight of biologic development. Nanobodies are proving themselves to be a potent complement to traditional mAb therapies, showing success in the treatment of, for example, autoimmune diseases and cancer, and more recently as therapeutic options to treat infectious diseases caused by rapidly evolving biological targets such as the SARS-CoV-2 virus. This review highlights the benefits of applying a proteomic approach to identify diverse nanobody sequences against a single antigen. This proteomic approach coupled with conventional yeast/phage display methods enables the production of highly diverse repertoires of nanobodies able to bind the vast epitope landscape of an antigen, with epitope sampling surpassing that of mAbs. Additionally, we aim to highlight recent findings illuminating the structural attributes of nanobodies that make them particularly amenable to comprehensive antigen sampling and to synergistic activity—underscoring the powerful advantage of acquiring a large, diverse nanobody repertoire against a single antigen. Lastly, we highlight the efforts being made in the clinical development of nanobodies, which have great potential as powerful diagnostic reagents and treatment options, especially when targeting infectious disease agents.

Successful methods used to produce high-affinity nanobodies, with a focus on proteomic approaches.

Nanobody features enabling comprehensive sampling of an antigen’s surface.

Advantages of a large diverse repertoire of nanobodies against an antigen.

Nanobodies as promising therapeutics targeting infectious diseases, e.g.SARS-CoV-2.

Key challenges when creating a nanobody-based therapeutic.

This review summarizes successful, widely used methods to produce high-affinity nanobodies against an antigen. We discuss the structural attributes of nanobodies that enable them to comprehensively sample their antigen surface and to engage in synergy pairs—underscoring the powerful advantages of acquiring a large, diverse nanobody repertoire against a single antigen. Lastly, we highlight the efforts being made in the development of nanobody therapeutics, which have great potential as diagnostic reagents and treatment options, especially when targeting infectious disease agents.

[end paper 74]

[begin paper 75]

PMCID = 10891761

Title = Serial Llama Immunization with Various SARS-CoV-2 RBD Variants Induces Broad Spectrum Virus-Neutralizing Nanobodies

The emergence of SARS-CoV-2 mutant variants has posed a significant challenge to both the prevention and treatment of COVID-19 with anti-coronaviral neutralizing antibodies. The latest viral variants demonstrate pronounced resistance to the vast majority of human monoclonal antibodies raised against the ancestral Wuhan variant. Less is known about the susceptibility of the evolved virus to camelid nanobodies developed at the start of the pandemic. In this study, we compared nanobody repertoires raised in the same llama after immunization with Wuhan’s RBD variant and after subsequent serial immunization with a variety of RBD variants, including that of SARS-CoV-1. We show that initial immunization induced highly potent nanobodies, which efficiently protected Syrian hamsters from infection with the ancestral Wuhan virus. These nanobodies, however, mostly lacked the activity against SARS-CoV-2 omicron-pseudotyped viruses. In contrast, serial immunization with different RBD variants resulted in the generation of nanobodies demonstrating a higher degree of somatic mutagenesis and a broad range of neutralization. Four nanobodies recognizing distinct epitopes were shown to potently neutralize a spectrum of omicron variants, including those of the XBB sublineage. Our data show that nanobodies broadly neutralizing SARS-CoV-2 variants may be readily induced by a serial variant RBD immunization.

[end paper 75]

[begin paper 76]

PMCID = 7854682

Title = Anti-CfaE nanobodies provide broad cross-protection against major pathogenic enterotoxigenic Escherichia coli strains, with implications for vaccine design

Enterotoxigenic Escherichia coli (ETEC) is estimated to cause approximately 380,000 deaths annually during sporadic or epidemic outbreaks worldwide. Development of vaccines against ETEC is very challenging due to the vast heterogeneity of the ETEC strains. An effective vaccines would have to be multicomponent to provide coverage of over ten ETEC strains with genetic variabilities. There is currently no vaccine licensed to prevent ETEC. Nanobodies are successful new biologics in treating mucosal infectious disease as they recognize conserved epitopes on hypervariable pathogens. Cocktails consisting of multiple nanobodies could provide even broader epitope coverage at a lower cost compared to monoclonal antibodies. Identification of conserved epitopes by nanobodies can also assist reverse engineering of an effective vaccine against ETEC. By screening nanobodies from immunized llamas and a naïve yeast display library against adhesins of colonization factors, we identified single nanobodies that show cross-protective potency against eleven major pathogenic ETEC strains in vitro. Oral administration of nanobodies led to a significant reduction of bacterial colonization in animals. Moreover, nanobody-IgA fusion showed extended inhibitory activity in mouse colonization compared to commercial hyperimmune bovine colostrum product used for prevention of ETEC-induced diarrhea. Structural analysis revealed that nanobodies recognized a highly-conserved epitope within the putative receptor binding region of ETEC adhesins. Our findings support further rational design of a pan-ETEC vaccine to elicit robust immune responses targeting this conserved epitope.

[end paper 76]

[begin paper 77]

PMCID = 8463502

Title = Rapid generation of potent antibodies by autonomous hypermutation in yeast

The predominant approach for antibody generation remains animal immunization, which can yield exceptionally selective and potent antibody clones owing to the powerful evolutionary process of somatic hypermutation. However, animal immunization is inherently slow, not always accessible, and poorly compatible with many antigens. Here, we describe Autonomous Hypermutation yEast surfAce Display (AHEAD), a synthetic recombinant antibody generation technology that imitates somatic hypermutation inside engineered yeast. By encoding antibody fragments on an error-prone orthogonal DNA replication system, surface-displayed antibody repertoires continuously mutate through simple cycles of yeast culturing and enrichment for antigen binding to produce high-affinity clones in as little as 2 weeks. We applied AHEAD to generate potent nanobodies against the SARS-CoV-2 S glycoprotein, a GPCR, and other targets, offering a template for streamlined antibody generation at large.

[end paper 77]

[begin paper 78]

PMCID = 8324831

Title = A synthetic nanobody targeting RBD protects hamsters from SARS-CoV-2 infection

SARS-CoV-2, the causative agent of COVID-19, features a receptor-binding domain (RBD) for binding to the host cell ACE2 protein. Neutralizing antibodies that block RBD-ACE2 interaction are candidates for the development of targeted therapeutics. Llama-derived single-domain antibodies (nanobodies, ~15 kDa) offer advantages in bioavailability, amenability, and production and storage owing to their small sizes and high stability. Here, we report the rapid selection of 99 synthetic nanobodies (sybodies) against RBD by in vitro selection using three libraries. The best sybody, MR3 binds to RBD with high affinity (KD = 1.0 nM) and displays high neutralization activity against SARS-CoV-2 pseudoviruses (IC50 = 0.42 μg mL−1). Structural, biochemical, and biological characterization suggests a common neutralizing mechanism, in which the RBD-ACE2 interaction is competitively inhibited by sybodies. Various forms of sybodies with improved potency have been generated by structure-based design, biparatopic construction, and divalent engineering. Two divalent forms of MR3 protect hamsters from clinical signs after live virus challenge and a single dose of the Fc-fusion construct of MR3 reduces viral RNA load by 6 Log10. Our results pave the way for the development of therapeutic nanobodies against COVID-19 and present a strategy for rapid development of targeted medical interventions during an outbreak.

Here, the authors report the engineering, structural and biological characterization of synthetic nanobodies (sybodies) that display potent therapeutic activity against SARS-CoV-2 infection in animal models via targeting the virus receptor-binding domain.

[end paper 78]

[begin paper 79]

PMCID = 8043454

Title = Nanobody Repertoires for Exposing Vulnerabilities of SARS-CoV-2

Despite the great promise of vaccines, the COVID-19 pandemic is ongoing and future serious outbreaks are highly likely, so that multi-pronged containment strategies will be required for many years. Nanobodies are the smallest naturally occurring single domain antigen binding proteins identified to date, possessing numerous properties advantageous to their production and use. We present a large repertoire of high affinity nanobodies against SARS-CoV-2 Spike protein with excellent kinetic and viral neutralization properties, which can be strongly enhanced with oligomerization. This repertoire samples the epitope landscape of the Spike ectodomain inside and outside the receptor binding domain, recognizing a multitude of distinct epitopes and revealing multiple neutralization targets of pseudoviruses and authentic SARS-CoV-2, including in primary human airway epithelial cells. Combinatorial nanobody mixtures show highly synergistic activities, and are resistant to mutational escape and emerging viral variants of concern. These nanobodies establish an exceptional resource for superior COVID-19 prophylactics and therapeutics.

[end paper 79]

[begin paper 80]

PMCID = 8465657

Title = A Small Virus to Deliver Small Antibodies: New Targeted Therapies Based on AAV Delivery of Nanobodies

Nanobodies are camelid-derived single-domain antibodies that present some advantages versus conventional antibodies, such as a smaller size, and higher tissue penetrability, stability, and hydrophilicity. Although nanobodies can be delivered as proteins, in vivo expression from adeno-associated viral (AAV) vectors represents an attractive strategy. This is due to the fact that AAV vectors, that can provide long-term expression of recombinant genes, have shown an excellent safety profile, and can accommodate genes for one or several nanobodies. In fact, several studies showed that AAV vectors can provide sustained nanobody expression both locally or systemically in preclinical models of human diseases. Some of the pathologies addressed with this technology include cancer, neurological, cardiovascular, infectious, and genetic diseases. Depending on the indication, AAV-delivered nanobodies can be expressed extracellularly or inside cells. Intracellular nanobodies or “intrabodies” carry out their function by interacting with cell proteins involved in disease and have also been designed to help elucidate cellular mechanisms by interfering with normal cell processes. Finally, nanobodies can also be used to retarget AAV vectors, when tethered to viral capsid proteins. This review covers applications in which AAV vectors have been used to deliver nanobodies, with a focus on their therapeutic use.

[end paper 80]

[begin paper 81]

PMCID = 8811630

Title = Biparatopic nanobodies protect mice from lethal challenge with SARS‐CoV‐2 variants of concern

The ongoing COVID‐19 pandemic and the emergence of new SARS‐CoV‐2 variants of concern (VOCs) requires continued development of effective therapeutics. Recently, we identified high‐affinity neutralizing nanobodies (Nbs) specific for the receptor‐binding domain (RBD) of SARS‐CoV‐2. Taking advantage of detailed epitope mapping, we generate two biparatopic Nbs (bipNbs) targeting a conserved epitope outside and two different epitopes inside the RBD:ACE2 interface. Both bipNbs bind all currently circulating VOCs with high affinities and are capable to neutralize cellular infection with VOC B.1.351 (Beta) and B.1.617.2 (Delta) in vitro. To assess if the bipNbs NM1267 and NM1268 confer protection against SARS‐CoV‐2 infection in vivo, human ACE2 transgenic mice are treated intranasally before infection with a lethal dose of SARS‐CoV‐2 B.1, B.1.351 (Beta) or B.1.617.2 (Delta). Nb‐treated mice show significantly reduced disease progression and increased survival rates. Histopathological analyses further reveal a drastically reduced viral load and inflammatory response in lungs. These data suggest that both bipNbs are broadly active against a variety of emerging SARS‐CoV‐2 VOCs and represent easily applicable drug candidates.

This study reports on two highly efficient RBD‐specific biparatopic nanobodies that bind and neutralize SARS‐CoV‐2 and its currently circulating variants of concern in vitro and in vivo, underscoring the potential of nanobodies to prevent or treat SARS‐CoV‐2 infection. 

[end paper 81]

[begin paper 82]

PMCID = 8928829

Title = Nebulized delivery of a broadly neutralizing SARS-CoV-2 RBD-specific nanobody prevents clinical, virological, and pathological disease in a Syrian hamster model of COVID-19

There remains an unmet need for globally deployable, low-cost therapeutics for the ongoing severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) pandemic. Previously, we reported on the isolation and in vitro characterization of a potent single-domain nanobody, NIH-CoVnb-112, specific for the receptor-binding domain (RBD) of SARS-CoV-2. Here, we report on the molecular basis for the observed broad in vitro neutralization capability of NIH-CoVnb-112 against variant SARS-CoV-2 pseudoviruses. The structure of NIH-CoVnb-112 bound to SARS-CoV-2 RBD reveals a large contact surface area overlapping the angiotensin converting enzyme 2 (ACE2) binding site, which is largely unencumbered by the common RBD mutations. In an in vivo pilot study, we demonstrate effective reductions in weight loss, viral burden, and lung pathology in a Syrian hamster model of COVID-19 following nebulized delivery of NIH-CoVnb-112. These findings support the further development of NIH-CoVnb-112 as a potential adjunct preventative therapeutic for the treatment of SARS-CoV-2 infection.

Abbreviations: ACE2 – angiotensin converting enzyme 2BSA – buried surface areaCDR – complementary determining regionRBD – receptor binding domainRBM – receptor-binding motifSARS-CoV-2 - severe acute respiratory syndrome coronavirus 2

[end paper 82]

[begin paper 83]

PMCID = 9063451

Title = Neutralizing Dromedary-Derived Nanobodies Against BotI-Like Toxin From the Most Hazardous Scorpion Venom in the Middle East and North Africa Region

Scorpion envenoming is a severe health problem in many regions causing significant clinical toxic effects and fatalities. In the Middle East/North Africa (MENA) region, Buthidae scorpion stings are responsible for devastating toxic outcomes in human. The only available specific immunotherapeutic treatment is based on IgG fragments of animal origin. To overcome the limitations of classical immunotherapy, we have demonstrated the in vivo efficacy of NbF12-10 bispecific nanobody at preclinical level. Nanobodies were developed against BotI analogues belonging to a distinct structural and antigenic group of scorpion toxins, occurring in the MENA region. From Buthus occitanus tunetanus venom, BotI-like toxin was purified. The 41 N-terminal amino acid residues were sequenced, and the LD50 was estimated at 40 ng/mouse. The BotI-like toxin was used for dromedary immunization. An immune VHH library was constructed, and after screening, two nanobodies were selected with nanomolar and sub-nanomolar affinity and recognizing an overlapping epitope. NbBotI-01 was able to neutralize 50% of the lethal effect of 13 LD50 BotI-like toxins in mice when injected by i.c.v route, whereas NbBotI-17 neutralized 50% of the lethal effect of 7 LD50. Interestingly, NbBotI-01 completely reduced the lethal effect of the 2 LD50 of BotG50 when injected at 1:4 molar ratio excess. More interestingly, an equimolar mixture of NbBotI-01 with NbF12-10 neutralized completely the lethal effect of 7 and 5 LD50 of BotG50 or AahG50, at 1:4 and 1:2 molar ratio, respectively. Hence, NbBotI-01 and NbF12-10 display synergic effects, leading to a novel therapeutic candidate for treating Buthus occitanus scorpion stings in the MENA region.

[end paper 83]

[begin paper 84]

PMCID = 10518403

Title = Unleashing the power of shark variable single domains (VNARs): broadly neutralizing tools for combating SARS-CoV-2

The pandemic caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) generated a joint global effort to develop vaccines and other treatments that could mitigate the negative effects and the rapid spread of the virus. Single-domain antibodies derived from various sources, including cartilaginous fish, camelids, and humans, have gained attention as promising therapeutic tools against coronavirus disease 2019. Shark-derived variable new antigen receptors (VNARs) have emerged as the smallest naturally occurring antigen-binding molecules. Here, we compile and review recent published studies on VNARs with the capacity to recognize and/or neutralize SARS-CoV-2. We found a close balance between the use of natural immune libraries and synthetic VNAR libraries for the screening against SARS-CoV-2, with phage display being the preferred display technology for the selection of VNARs against this virus. In addition, we discuss potential modifications and engineering strategies employed to improve the neutralization potential of VNARs, such as exploring fusion with the Fc domain of human Immunoglobulin G (IgG) to increase avidity and therapeutic potential. This research highlights the potential of VNARs as powerful molecular tools in the fight against infectious diseases.

[end paper 84]

[begin paper 85]

PMCID = 8828845

Title = An ultrapotent RBD-targeted biparatopic nanobody neutralizes broad SARS-CoV-2 variants

The wide transmission and host adaptation of SARS-CoV-2 have led to the rapid accumulation of mutations, posing significant challenges to the effectiveness of vaccines and therapeutic antibodies. Although several neutralizing antibodies were authorized for emergency clinical use, convalescent patients derived natural antibodies are vulnerable to SARS-CoV-2 Spike mutation. Here, we describe the screen of a panel of SARS-CoV-2 receptor-binding domain (RBD) targeted nanobodies (Nbs) from a synthetic library and the design of a biparatopic Nb, named Nb1–Nb2, with tight affinity and super-wide neutralization breadth against multiple SARS-CoV-2 variants of concern. Deep-mutational scanning experiments identify the potential binding epitopes of the Nbs on the RBD and demonstrate that biparatopic Nb1–Nb2 has a strong escape-resistant feature against more than 60 tested RBD amino acid substitutions. Using pseudovirion-based and trans-complementation SARS-CoV-2 tools, we determine that the Nb1–Nb2 broadly neutralizes multiple SARS-CoV-2 variants at sub-nanomolar levels, including Alpha (B.1.1.7), Beta (B.1.351), Gamma (P.1), Delta (B.1.617.2), Lambda (C.37), Kappa (B.1.617.1), and Mu (B.1.621). Furthermore, a heavy-chain antibody is constructed by fusing the human IgG1 Fc to Nb1–Nb2 (designated as Nb1–Nb2-Fc) to improve its neutralization potency, yield, stability, and potential half-life extension. For the new Omicron variant (B.1.1.529) that harbors unprecedented multiple RBD mutations, Nb1–Nb2-Fc keeps a firm affinity (KD < 1.0 × 10−12 M) and strong neutralizing activity (IC50 = 1.46 nM for authentic Omicron virus). Together, we developed a tetravalent biparatopic human heavy-chain antibody with ultrapotent and broad-spectrum SARS-CoV-2 neutralization activity which highlights the potential clinical applications.

[end paper 85]

[begin paper 86]

PMCID = 9529347

Title = Biparatopic nanobodies targeting the receptor binding domain efficiently neutralize SARS-CoV-2

The development of therapeutics to prevent or treat COVID-19 remains an area of intense focus. Protein biologics, including monoclonal antibodies and nanobodies that neutralize virus, have potential for the treatment of active disease. Here, we have used yeast display of a synthetic nanobody library to isolate nanobodies that bind the receptor-binding domain (RBD) of SARS-CoV-2 and neutralize the virus. We show that combining two clones with distinct binding epitopes within the RBD into a single protein construct to generate biparatopic reagents dramatically enhances their neutralizing capacity. Furthermore, the biparatopic nanobodies exhibit enhanced control over clinically relevant RBD variants that escaped recognition by the individual nanobodies. Structural analysis of biparatopic binding to spike (S) protein revealed a unique binding mode whereby the two nanobody paratopes bridge RBDs encoded by distinct S trimers. Accordingly, biparatopic nanobodies offer a way to rapidly generate powerful viral neutralizers with enhanced ability to control viral escape mutants.

Yeast display was used to generate SARS-CoV-2 RBD-specific nanobodies

Distinct nanobody clones were fused to create biparatopic reagents

Biparatopic nanobodies protect mice from SARS-CoV-2 infection

The biparatopics bridge distinct S proteins in a unique “twinned-S” conformation

Immunology; Microbiology; Structural biology.

[end paper 86]

[begin paper 87]

PMCID = 9174178

Title = Superimmunity by pan-sarbecovirus nanobodies

Vaccine boosters and infection can facilitate the development of SARS-CoV-2 antibodies with improved potency and breadth. Here, we observe superimmunity in a camelid extensively immunized with the SARS-CoV-2 receptor-binding domain (RBD). We rapidly isolate a large repertoire of specific ultra-high-affinity nanobodies that bind strongly to all known sarbecovirus clades using integrative proteomics. These pan-sarbecovirus nanobodies (psNbs) are highly effective against SARS-CoV and SARS-CoV-2 variants, including Omicron, with the best median neutralization potency at single-digit nanograms per milliliter. A highly potent, inhalable, and bispecific psNb (PiN-31) is also developed. Structural determinations of 13 psNbs with the SARS-CoV-2 spike or RBD reveal five epitope classes, providing insights into the mechanisms and evolution of their broad activities. The highly evolved psNbs target small, flat, and flexible epitopes that contain over 75% of conserved RBD surface residues. Their potencies are strongly and negatively correlated with the distance of the epitopes from the receptor binding sites.

Xiang et al. characterize 100 diverse pan-sarbecovirus nanobodies (psNbs) that are highly effective against SARS-CoV and SARS-CoV-2 variants, including Omicron, with the best median neutralization potency at single-digit nanograms per milliliter. Structural determinations of 13 psNbs reveal five RBD epitope classes, providing insights into the mechanisms and evolution of their broad activities.

[end paper 87]

[begin paper 88]

PMCID = 10588750

Title = A Naïve Phage Display Library-Derived Nanobody Neutralizes SARS-CoV-2 and Three Variants of Concern

The emergence of the coronavirus disease 2019 (COVID-19) pandemic and the new severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) variants of concern (VOCs) requires the continuous development of safe, effective, and affordable prevention and therapeutics. Nanobodies have demonstrated antiviral activity against a variety of viruses, providing a new candidate for the prevention and treatment of SARS-CoV-2 and its variants.

SARS-CoV-2 glycoprotein spike 1 subunit (S1) was selected as the target antigen for nanobody screening of a naïve phage display library. We obtained a nanobody, named Nb-H6, and then determined its affinity, inhibition, and stability by ELISA, Competitive ELISA, and Biolayer Interferometry (BLI). Infection assays of authentic and pseudotyped SARS-CoV-2 were performed to evaluate the neutralization of Nb-H6. The structure and mechanism of action were investigated by AlphaFold, docking, and residue mutation assays.

We isolated and characterized a nanobody, Nb-H6, which exhibits a broad affinity for S1 and the receptor binding domain (RBD) of SARS-CoV-2, or Alpha (B.1.1.7), Delta (B.1.617.2), Lambda (C.37), and Omicron (BA.2 and BA.5), and blocks receptor angiotensin-converting enzyme 2 (ACE2) binding. Moreover, Nb-H6 can retain its binding capability after pH or thermal treatment and effectively neutralize both pseudotyped and authentic SARS-CoV-2, as well as VOC Alpha (B.1.1.7), Delta (B.1.617.2), and Omicron (BA.2 and BA.5) pseudoviruses. We also confirmed that Nb-H6 binds two distinct amino acid residues of the RBD, preventing SARS-CoV-2 from interacting with the host receptor.

Our study highlights a novel nanobody, Nb-H6, that may be useful therapeutically in SARS-CoV-2 and VOC outbreaks and pandemics. These findings also provide a molecular foundation for further studies into how nanobodies neutralize SARS-CoV-2 and variants and imply potential therapeutic targets for the treatment of COVID-19.

[end paper 88]

[begin paper 89]

PMCID = 9896449

Title = Shark nanobodies with potent SARS-CoV-2 neutralizing activity and broad sarbecovirus reactivity

Despite rapid and ongoing vaccine and therapeutic development, SARS-CoV-2 continues to evolve and evade, presenting a need for next-generation diverse therapeutic modalities. Here we show that nurse sharks immunized with SARS-CoV-2 recombinant receptor binding domain (RBD), RBD-ferritin (RFN), or spike protein ferritin nanoparticle (SpFN) immunogens elicit a set of new antigen receptor antibody (IgNAR) molecules that target two non-overlapping conserved epitopes on the spike RBD. Representative shark antibody variable NAR-Fc chimeras (ShAbs) targeting either of the two epitopes mediate cell-effector functions, with high affinity to all SARS-CoV-2 viral variants of concern, including the divergent Omicron strains. The ShAbs potently cross-neutralize SARS-CoV-2 WA-1, Alpha, Beta, Delta, Omicron BA.1 and BA.5, and SARS-CoV-1 pseudoviruses, and confer protection against SARS-CoV-2 challenge in the K18-hACE2 transgenic mouse model. Structural definition of the RBD-ShAb01-ShAb02 complex enabled design and production of multi-specific nanobodies with enhanced neutralization capacity, and picomolar affinity to divergent sarbecovirus clade 1a, 1b and 2 RBD molecules. These shark nanobodies represent potent immunotherapeutics both for current use, and future sarbecovirus pandemic preparation.

SARS-CoV-2 variants of concern continue to emerge, reducing vaccine efficacy and limiting therapeutic options. Here, Chen and colleagues describe the identification and design of shark nanobodies with pansarbecovirus activity.

[end paper 89]

[begin paper 90]

PMCID = 7430568

Title = An ultra-potent synthetic nanobody neutralizes SARS-CoV-2 by locking Spike into an inactive conformation

Without an effective prophylactic solution, infections from SARS-CoV-2 continue to rise worldwide with devastating health and economic costs. SARS-CoV-2 gains entry into host cells via an interaction between its Spike protein and the host cell receptor angiotensin converting enzyme 2 (ACE2). Disruption of this interaction confers potent neutralization of viral entry, providing an avenue for vaccine design and for therapeutic antibodies. Here, we develop single-domain antibodies (nanobodies) that potently disrupt the interaction between the SARS-CoV-2 Spike and ACE2. By screening a yeast surface-displayed library of synthetic nanobody sequences, we identified a panel of nanobodies that bind to multiple epitopes on Spike and block ACE2 interaction via two distinct mechanisms. Cryogenic electron microscopy (cryo-EM) revealed that one exceptionally stable nanobody, Nb6, binds Spike in a fully inactive conformation with its receptor binding domains (RBDs) locked into their inaccessible down-state, incapable of binding ACE2. Affinity maturation and structure-guided design of multivalency yielded a trivalent nanobody, mNb6-tri, with femtomolar affinity for SARS-CoV-2 Spike and picomolar neutralization of SARS-CoV-2 infection. mNb6-tri retains stability and function after aerosolization, lyophilization, and heat treatment. These properties may enable aerosol-mediated delivery of this potent neutralizer directly to the airway epithelia, promising to yield a widely deployable, patient-friendly prophylactic and/or early infection therapeutic agent to stem the worst pandemic in a century.

[end paper 90]

[begin paper 91]

PMCID = 10054972

Title = Nanobodies against SARS-CoV-2 reduced virus load in the brain of challenged mice and neutralized Wuhan, Delta and Omicron Variants

In this work, we developed llama-derived nanobodies (Nbs) directed to the receptor binding domain (RBD) and other domains of the Spike (S) protein of SARS-CoV-2. Nanobodies were selected after the biopanning of two VHH-libraries, one of which was generated after the immunization of a llama (lama glama) with the bovine coronavirus (BCoV) Mebus, and another with the full-length pre-fused locked S protein (S-2P) and the RBD from the SARS-CoV-2 Wuhan strain (WT). Most of the neutralizing Nbs selected with either RBD or S-2P from SARS-CoV-2 were directed to RBD and were able to block S-2P/ACE2 interaction. Three Nbs recognized the N-terminal domain (NTD) of the S-2P protein as measured by competition with biliverdin, while some non-neutralizing Nbs recognize epitopes in the S2 domain. One Nb from the BCoV immune library was directed to RBD but was non-neutralizing. Intranasal administration of Nbs induced protection ranging from 40% to 80% against COVID-19 death in k18-hACE2 mice challenged with the WT strain. Interestingly, protection was not only associated with a significant reduction of virus replication in nasal turbinates and lungs, but also with a reduction of virus load in the brain. Employing pseudovirus neutralization assays, we were able to identify Nbs with neutralizing capacity against the Alpha, Beta, Delta and Omicron variants. Furthermore, cocktails of different Nbs performed better than individual Nbs to neutralize two Omicron variants (B.1.529 and BA.2). Altogether, the data suggest these Nbs can potentially be used as a cocktail for intranasal treatment to prevent or treat COVID-19 encephalitis, or modified for prophylactic administration to fight this disease.

[end paper 91]

[begin paper 92]

PMCID = 5754017

Title = Using Homology Modeling to Interrogate Binding Affinity in Neutralization of Ricin Toxin by a Family of Single Domain Antibodies

In this report we investigated, within a group of closely related single domain camelid antibodies (VHHs), the relationship between binding affinity and neutralizing activity as it pertains to ricin, a fast-acting toxin and biothreat agent. The V1C7-like VHHs (V1C7, V2B9, V2E8, and V5C1) are similar in amino acid sequence, but differ in their binding affinities and toxin-neutralizing activities. Using the X-ray crystal structure of V1C7 in complex with ricin’s enzymatic subunit (RTA) as a template, Rosetta-based homology modeling coupled with energetic decomposition led us to predict that a single pairwise interaction between Arg29 on V5C1 and Glu67 on RTA was responsible for the difference in ricin toxin binding affinity between V1C7, a weak neutralizer, and V5C1, a moderate neutralizer. This prediction was borne out experimentally: substitution of Arg for Gly at position 29 enhanced V1C7’s binding affinity for ricin, whereas the reverse (i.e., Gly for Arg at position 29) diminished V5C1’s binding affinity by >10 fold. As expected, the V5C1R29G mutant was largely devoid of toxin-neutralizing activity. However, the toxin-neutralizing activity of the V1C7G29R mutant was not correspondingly improved, indicating that in the V1C7 family binding affinity alone does not account for differences in antibody function. V1C7 and V5C1, as well as their respective point mutants, recognized indistinguishable epitopes on RTA, at least at the level of sensitivity afforded by hydrogen-deuterium mass spectrometry. The results of this study have implications for engineering therapeutic antibodies because they demonstrate that even subtle differences in epitope specificity can account for important differences in antibody function.

[end paper 92]

[begin paper 93]

PMCID = 10858526

Title = Targeted drug delivery using nanobodies to deliver effective molecules to breast cancer cells: the most attractive application of nanobodies

Targeted drug delivery is one of the attractive ways in which cancer treatment can significantly reduce side effects. In the last two decades, the use of antibodies as a tool for accurate detection of cancer has been noted. On the other hand, the binding of drugs and carriers containing drugs to the specific antibodies of cancer cells can specifically target only these cells. However, the use of whole antibodies brings challenges, including their large size, the complexity of conjugation, the high cost of production, and the creation of immunogenic reactions in the body. The use of nanobodies, or VHHs, which are a small part of camel heavy chain antibodies, is very popular due to their small size, high craftsmanship, and low production cost. In this article, in addition to a brief overview of the structure and characteristics of nanobodies, the use of this molecule in the targeted drug delivery of breast cancer has been reviewed.

[end paper 93]

[begin paper 94]

PMCID = 10275483

Title = Emerging Landscape of Nanobodies and Their Neutralizing Applications against SARS-CoV-2 Virus

The new severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) that causes the coronavirus disease 2019 (COVID-19) has significantly altered people’s way of life. Despite widespread knowledge of vaccination, mask use, and avoidance of close contact, COVID-19 is still spreading around the world. Numerous research teams are examining the SARS-CoV-2 infection process to discover strategies to identify, prevent, and treat COVID-19 to limit the spread of this chronic coronavirus illness and restore lives to normalcy. Nanobodies have advantages over polyclonal and monoclonal antibodies (Ab) and Ab fragments, including reduced size, high stability, simplicity in manufacture, compatibility with genetic engineering methods, and lack of solubility and aggregation issues. Recent studies have shown that nanobodies that target the SARS-CoV-2 receptor-binding domain and disrupt ACE2 interactions are helpful in the prevention and treatment of SARS-CoV-2-infected animal models, despite the lack of evidence in human patients. The creation and evaluation of nanobodies, as well as their diagnostic and therapeutic applications against COVID-19, are discussed in this paper.

[end paper 94]

[begin paper 95]

PMCID = 9113008

Title = SARS-CoV-2 Delta Variant Decreases Nanobody Binding and ACE2 Blocking Effectivity

The Delta variant spreads more rapidly than previous variants of SARS-CoV-2. This variant comprises several mutations on the receptor-binding domain (RBDDelta) of its spike glycoprotein, which binds to the peptidase domain (PD) of angiotensin-converting enzyme 2 (ACE2) receptors in host cells. The RBD–PD interaction has been targeted by antibodies and nanobodies to prevent viral infection, but their effectiveness against the Delta variant remains unclear. Here, we investigated RBDDelta–PD interactions in the presence and absence of nanobodies H11-H4, H11-D4, and Ty1 by performing 21.8 μs of all-atom molecular dynamics simulations. Unbiased simulations revealed that Delta variant mutations strengthen RBD binding to ACE2 by increasing the hydrophobic interactions and salt bridge formation, but weaken interactions with H11-H4, H11-D4, and Ty1. Among these nanobodies H11-H4 and H11-D4 bind RBD without overlapping ACE2. They were unable to dislocate ACE2 from RBDDelta when bound side by side with ACE2 on RBD. Steered molecular dynamics simulations at comparable loading rates to high-speed atomic force microscopy (AFM) experiments estimated lower rupture forces of the nanobodies from RBDDelta compared to ACE2. Our results suggest that existing nanobodies are less effective to inhibit RBDDelta–PD interactions and a new generation of nanobodies is needed to neutralize the Delta variant.

[end paper 95]

[begin paper 96]

PMCID = 11228696

Title = Current development of severe acute respiratory syndrome coronavirus 2 neutralizing antibodies (Review)

The coronavirus disease 2019 pandemic due to severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) seriously affected global public health security. Studies on vaccines, neutralizing antibodies (NAbs) and small molecule antiviral drugs are currently ongoing. In particular, NAbs have emerged as promising therapeutic agents due to their well-defined mechanism, high specificity, superior safety profile, ease of large-scale production and simultaneous application for both prevention and treatment of viral infection. Numerous NAb therapeutics have entered the clinical research stages, demonstrating promising therapeutic and preventive effects. These agents have been used for outbreak prevention and control under urgent authorization processes. The present review summarizes the molecular targets of SARS-CoV-2-associated NAbs and screening and identification techniques for NAb development. Moreover, the current shortcomings and challenges that persist with the use of NAbs are discussed. The aim of the present review is to offer a reference for the development of NAbs for any future emergent infectious diseases, including SARS-CoV-2.

[end paper 96]

[begin paper 97]

PMCID = 9132424

Title = Deep mutational engineering of broadly-neutralizing nanobodies accommodating SARS-CoV-1 and 2 antigenic drift

Here, we report the molecular engineering of nanobodies that bind with picomolar affinity to both SARS-CoV-1 and SARS-CoV-2 receptor-binding domains (RBD) and are highly neutralizing. We applied deep mutational engineering to VHH72, a nanobody initially specific for SARS-CoV-1 RBD with little cross-reactivity to SARS-CoV-2 antigen. We first identified all the individual VHH substitutions that increase binding to SARS-CoV-2 RBD and then screened highly focused combinatorial libraries to isolate engineered nanobodies with improved properties. The corresponding VHH-Fc molecules show high affinities for SARS-CoV-2 antigens from various emerging variants and SARS-CoV-1, block the interaction between ACE2 and RBD, and neutralize the virus with high efficiency. Its rare specificity across sarbecovirus relies on its peculiar epitope outside the immunodominant regions. The engineered nanobodies share a common motif of three amino acids, which contribute to the broad specificity of recognition. Our results show that deep mutational engineering is a very powerful method, especially to rapidly adapt existing antibodies to new variants of pathogens.

[end paper 97]

[begin paper 98]

PMCID = 8451865

Title = Development of a platform process for the production and purification of single‐domain antibodies

Single‐domain antibodies (sdAbs) offer the affinity and therapeutic value of conventional antibodies, with increased stability and solubility. Unlike conventional antibodies, however, sdAbs do not benefit from a platform manufacturing process. While successful production of a variety of sdAbs has been shown in numerous hosts, purification methods are often molecule specific or require affinity tags, which generally cannot be used in clinical manufacturing due to regulatory concerns. Here, we have developed a broadly applicable production and purification process for sdAbs in Komagataella phaffii (Pichia pastoris) and demonstrated the production of eight different sdAbs at a quality appropriate for nonclinical studies. We developed a two‐step, integrated purification process without the use of affinity resins and showed that modification of a single process parameter, pH of the bridging buffer, was required for the successful purification of a variety of sdAbs. Further, we determined that this parameter can be predicted based only on the biophysical characteristics of the target molecule. Using these methods, we produced nonclinical quality sdAbs as few as 5 weeks after identifying the product sequence. Nonclinical studies of three different sdAbs showed that molecules produced using our platform process conferred protection against viral shedding of rotavirus or H1N1 influenza and were equivalent to similar molecules produced in Escherichia coli and purified using affinity tags.

Unlike conventional antibodies, single‐domain antibodies (sdAbs) do not benefit from a platform manufacturing process, meaning that each new sdAb requires extensive process development to be produced and purified. We present here a platform process which can be used to produce phase‐appropriate, tag‐less sdAbs with nonclinical quality as few as five weeks after obtaining the target product sequence, and show that molecules produced using this process are comparable to the same sdAbs produced using affinity tag chromatography in nonclinical studies. 

[end paper 98]

[begin paper 99]

PMCID = 10597523

Title = Computational design of novel nanobodies targeting the receptor binding domain of variants of concern of SARS-CoV-2

The COVID-19 pandemic has created an urgent need for effective therapeutic and diagnostic strategies to manage the disease caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). However, the emergence of numerous variants of concern (VOCs) has made it challenging to develop targeted therapies that are broadly specific in neutralizing the virus. In this study, we aimed to develop neutralizing nanobodies (Nbs) using computational techniques that can effectively neutralize the receptor-binding domain (RBD) of SARS-CoV-2 VOCs. We evaluated the performance of different protein-protein docking programs and identified HDOCK as the most suitable program for Nb/RBD docking with high accuracy. Using this approach, we designed 14 novel Nbs with high binding affinity to the VOC RBDs. The Nbs were engineered with mutated amino acids that interacted with key amino acids of the RBDs, resulting in higher binding affinity than human angiotensin-converting enzyme 2 (ACE2) and other viral RBDs or haemagglutinins (HAs). The successful development of these Nbs demonstrates the potential of molecular modeling as a low-cost and time-efficient method for engineering effective Nbs against SARS-CoV-2. The engineered Nbs have the potential to be employed in RBD-neutralizing assays, facilitating the identification of novel treatment, prevention, and diagnostic strategies against SARS-CoV-2.

[end paper 99]

[begin paper 100]

PMCID = 8700021

Title = Epitope profiling using computational structural modelling demonstrated on coronavirus-binding antibodies

Identifying the epitope of an antibody is a key step in understanding its function and its potential as a therapeutic. Sequence-based clonal clustering can identify antibodies with similar epitope complementarity, however, antibodies from markedly different lineages but with similar structures can engage the same epitope. We describe a novel computational method for epitope profiling based on structural modelling and clustering. Using the method, we demonstrate that sequence dissimilar but functionally similar antibodies can be found across the Coronavirus Antibody Database, with high accuracy (92% of antibodies in multiple-occupancy structural clusters bind to consistent domains). Our approach functionally links antibodies with distinct genetic lineages, species origins, and coronavirus specificities. This indicates greater convergence exists in the immune responses to coronaviruses than is suggested by sequence-based approaches. Our results show that applying structural analytics to large class-specific antibody databases will enable high confidence structure-function relationships to be drawn, yielding new opportunities to identify functional convergence hitherto missed by sequence-only analysis.

Antibodies are a key component of the immune system that combat pathogens by binding to a defined region of their molecular surface (known as an ‘epitope’). The ability to map which antibodies target the same epitopes is crucial when designing non-competing antibody therapeutics or predicting the influence of pathogen mutation on population immunity. While one can use laboratory experiments to deduce when pairs of antibodies engage the same epitope, such experiments are very expensive and time consuming if used to compare on the order of thousands of antibodies. In this work, we report a new computational algorithm (SPACE) that clusters antibodies that target the same epitope based on their predicted 3D structure, as binding site structure is a property often conserved between binders complementary to the same epitope. Unlike existing antibody epitope profiling tools which assume two antibodies must share a high sequence identity/similar genetic basis to engage the same region, our orthogonal method can detect broader patterns of convergent evolution across binders to different pathogen strains, and between antibodies with different genetic and even species origins.

[end paper 100]



