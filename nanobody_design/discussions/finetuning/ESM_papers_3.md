## User

This is the beginning of an individual meeting with Machine Learning Specialist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. You are responsible for understanding the topic "ESM" in the context of designing nanobody binders for SARS-CoV-2. You need to fine-tune yourself on the relevant literature on ESM to improve your ability to design SARS-CoV-2 nanobody binders. Please use PubMed Central and search for relevant papers on ESM using the query "ESM SARS-CoV-2 spike protein binding" and request 100 articles with abstracts only. Read all of the abstracts and based on each abstract individually, decide whether you want to fine-tune yourself on the full text of that paper. Include as many papers as possible, but only include papers that are directly relevant to ESM. Please provide the PMCIDs and titles of all the papers that you wish to fine-tune yourself on as a Python dictionary mapping PMCID as a double-quoted string to title as a double-quoted string.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Machine Learning Specialist, please provide your response to the agenda.

## Machine Learning Specialist

Based on the abstracts provided, here are the papers that are directly relevant to ESM (Evolutionary Scale Modeling) in the context of designing nanobody binders for SARS-CoV-2, and which I would like to fine-tune myself on:

```python
{
    "11725859": "Learning the language of antibody hypervariability",
    "10942297": "Novel antibody language model accelerates IgG screening and design for broad-spectrum antiviral therapy",
    "11614202": "Prediction of virus-host associations using protein language models and multiple instance learning",
    "10869273": "Efficient evolution of human antibodies from general protein language models",
    "10831124": "Binding affinity between coronavirus spike protein and human ACE2 receptor"
}
```

These papers focus on the application of protein language models, including ESM, in the context of antibody design and prediction of interactions, which is directly relevant to the task of designing SARS-CoV-2 nanobody binders.

## User

Tool Output:

Here are the top 100 articles on PubMed Central for the query "ESM SARS-CoV-2 spike protein binding":

[begin paper 1]

PMCID = 10785701

Title = Differences in syncytia formation by SARS-CoV-2 variants modify host chromatin accessibility and cellular senescence via TP53

Coronavirus disease 2019 (COVID-19) remains a significant public health threat due to the ability of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) variants to evade the immune system and cause breakthrough infections. Although pathogenic coronaviruses such as SARS-CoV-2 and Middle East respiratory syndrome (MERS)-CoV lead to severe respiratory infections, how these viruses affect the chromatin proteomic composition upon infection remains largely uncharacterized. Here, we use our recently developed integrative DNA And Protein Tagging methodology to identify changes in host chromatin accessibility states and chromatin proteomic composition upon infection with pathogenic coronaviruses. SARS-CoV-2 infection induces TP53 stabilization on chromatin, which contributes to its host cytopathic effect. We mapped this TP53 stabilization to the SARS-CoV-2 spike and its propensity to form syncytia, a consequence of cell-cell fusion. Differences in SARS-CoV-2 spike variant-induced syncytia formation modify chromatin accessibility, cellular senescence, and inflammatory cytokine release via TP53. Our findings suggest that differences in syncytia formation alter senescence-associated inflammation, which varies among SARS-CoV-2 variants.

Lee et al. find that spike-mediated cell-cell fusion triggers TP53 stabilization, chromatin accessibility changes, and activation of senescence. The extent of these effects differs based on the fusogenicity of various SARS-CoV-2 variant spike sequences.

[end paper 1]

[begin paper 2]

PMCID = 10661752

Title = Infection and Vaccine Induced Spike Antibody Responses Against SARS-CoV-2 Variants of Concern in COVID-19-Naïve Children and Adults

Although a more efficient adaptive humoral immune response has been proposed to underlie the usually favorable outcome of pediatric COVID-19, the breadth of viral and vaccine cross-reactivity toward the ever-mutating Spike protein among variants of concern (VOCs) has not yet been compared between children and adults. We assessed antibodies to conformational Spike in COVID-19-naïve children and adults vaccinated by BNT162b2 and ChAdOx1, and naturally infected with SARS-CoV-2 Early Clade, Delta, and Omicron. Sera were analyzed against Spike including naturally occurring VOCs Alpha, Beta, Gamma, Delta, and Omicron BA.1, BA.2, BA.5, BQ.1.1, BA2.75.2, and XBB.1, and variants of interest Epsilon, Kappa, Eta, D.2, and artificial mutant Spikes. There was no notable difference between breadth and longevity of antibody against VOCs in children and adults. Vaccinated individuals displayed similar immunoreactivity profiles across variants compared with naturally infected individuals. Delta-infected patients had an enhanced cross-reactivity toward Delta and earlier VOCs compared to patients infected by Early Clade SARS-CoV-2. Although Omicron BA.1, BA.2, BA.5, BQ.1.1, BA2.75.2, and XBB.1 antibody titers were generated after Omicron infection, cross-reactive binding against Omicron subvariants was reduced across all infection, immunization, and age groups. Some mutations, such as 498R and 501Y, epistatically combined to enhance cross-reactive binding, but could not fully compensate for antibody-evasive mutations within the Omicron subvariants tested. Our results reveal important molecular features central to the generation of high antibody titers and broad immunoreactivity that should be considered in future vaccine design and global serosurveillance in the context of limited vaccine boosters available to the pediatric population.

The online version contains supplementary material available at 10.1007/s10875-023-01540-5.

[end paper 2]

[begin paper 3]

PMCID = 10356814

Title = Identifying and profiling structural similarities between Spike of SARS-CoV-2 and other viral or host proteins with Machaon

Using protein structure to predict function, interactions, and evolutionary history is still an open challenge, with existing approaches relying extensively on protein homology and families. Here, we present Machaon, a data-driven method combining orientation invariant metrics on phi-psi angles, inter-residue contacts and surface complexity. It can be readily applied on whole structures or segments—such as domains and binding sites. Machaon was applied on SARS-CoV-2 Spike monomers of native, Delta and Omicron variants and identified correlations with a wide range of viral proteins from close to distant taxonomy ranks, as well as host proteins, such as ACE2 receptor. Machaon’s meta-analysis of the results highlights structural, chemical and transcriptional similarities between the Spike monomer and human proteins, indicating a multi-level viral mimicry. This extended analysis also revealed relationships of the Spike protein with biological processes such as ubiquitination and angiogenesis and highlighted different patterns in virus attachment among the studied variants. Available at: https://machaonweb.com.

The presented method Machaon identifies similar whole structures or fragments with SARS-COV-2 Spike using alignment-free metrics on phi-psi angles, inter-residue contacts and surface complexity and enriches these relationships via meta-analysis.

[end paper 3]

[begin paper 4]

PMCID = 8165686

Title = Plausible blockers of Spike RBD in SARS-CoV2—molecular design and underlying interaction dynamics from high-level structural descriptors

COVID-19 is characterized by an unprecedented abrupt increase in the viral transmission rate (SARS-CoV-2) relative to its pandemic evolutionary ancestor, SARS-CoV (2003). The complex molecular cascade of events related to the viral pathogenicity is triggered by the Spike protein upon interacting with the ACE2 receptor on human lung cells through its receptor binding domain (RBDSpike). One potential therapeutic strategy to combat COVID-19 could thus be limiting the infection by blocking this key interaction. In this current study, we adopt a protein design approach to predict and propose non-virulent structural mimics of the RBDSpike which can potentially serve as its competitive inhibitors in binding to ACE2. The RBDSpike is an independently foldable protein domain, resilient to conformational changes upon mutations and therefore an attractive target for strategic re-design. Interestingly, in spite of displaying an optimal shape fit between their interacting surfaces (attributed to a consequently high mutual affinity), the RBDSpike–ACE2 interaction appears to have a quasi-stable character due to a poor electrostatic match at their interface. Structural analyses of homologous protein complexes reveal that the ACE2 binding site of RBDSpike has an unusually high degree of solvent-exposed hydrophobic residues, attributed to key evolutionary changes, making it inherently “reaction-prone.” The designed mimics aimed to block the viral entry by occupying the available binding sites on ACE2, are tested to have signatures of stable high-affinity binding with ACE2 (cross-validated by appropriate free energy estimates), overriding the native quasi-stable feature. The results show the apt of directly adapting natural examples in rational protein design, wherein, homology-based threading coupled with strategic “hydrophobic ↔ polar” mutations serve as a potential breakthrough.

The online version contains supplementary material available at 10.1007/s00894-021-04779-0.

[end paper 4]

[begin paper 5]

PMCID = 7577648

Title = Human Hematopoietic Stem, Progenitor, and Immune Cells Respond Ex Vivo to SARS-CoV-2 Spike Protein

Despite evidence that SARS-CoV-2 infection is systemic in nature, there is little known about the effects that SARS-CoV-2 infection or exposure has on many host cell types, including primitive and mature hematopoietic cells. The hematopoietic system is responsible for giving rise to the very immune cells that defend against viral infection and is a source of hematopoietic stem cells (HSCs) and progenitor cells (HPCs) which are used for hematopoietic cell transplantation (HCT) to treat hematologic disorders, thus there is a strong need to understand how exposure to the virus may affect hematopoietic cell functions. We examined the expression of ACE2, to which SARS-CoV-2 Spike (S) protein binds to facilitate viral entry, in cord blood derived HSCs/HPCs and in peripheral blood derived immune cell subtypes. ACE2 is expressed in low numbers of immune cells, higher numbers of HPCs, and up to 65% of rigorously defined HSCs. We also examined effects of exposing HSCs/HPCs and immune cells to SARS-CoV-2 S protein ex vivo. HSCs and HPCs expand less effectively and have less functional colony forming capacity when grown with S protein, while peripheral blood monocytes upregulate CD14 expression and show distinct changes in size and granularity. That these effects are induced by recombinant S protein alone and not the infectious viral particle suggests that simple exposure to SARS-CoV-2 may impact HSCs/HPCs and immune cells via S protein interactions with the cells, regardless of whether they can be infected. These data have implications for immune response to SARS-CoV-2 and for HCT.

• Human HSCs, HPCs, and immune cells express ACE2 on the cell surface, making them potentially susceptible to SARS-CoV-2 infection.

• SARS-CoV-2 S protein, which binds to ACE2, induces defects in the colony forming capacity of human HPC and inhibits the expansion of HSC/HPC subpopulations ex vivo. These effects can be at least partially neutralized by treatment with SARS-CoV-2 targeting antibody, recombinant human ACE2, or Angiotensin1–7.

• S protein also induces aberrant morphological changes in peripheral blood derived monocytes ex vivo.

• Thus, there are many different manners in which SARS-CoV-2 virus may impact the functional hematopoietic system, which has important implications for hematological manifestations of COVID-19 (i.e. thrombocytopenia and lymphopenia), immune response, and hematopoietic stem cell transplant in the era of COVID-19.

The online version of this article (10.1007/s12015-020-10056-z) contains supplementary material, which is available to authorized users.

[end paper 5]

[begin paper 6]

PMCID = 10831124

Title = Binding affinity between coronavirus spike protein and human ACE2 receptor

Coronaviruses (CoVs) pose a major risk to global public health due to their ability to infect diverse animal species and potential for emergence in humans. The CoV spike protein mediates viral entry into the cell and plays a crucial role in determining the binding affinity to host cell receptors. With particular emphasis on α- and β-coronaviruses that infect humans and domestic animals, current research on CoV receptor use suggests that the exploitation of the angiotensin-converting enzyme 2 (ACE2) receptor poses a significant threat for viral emergence with pandemic potential. This review summarizes the approaches used to study binding interactions between CoV spike proteins and the human ACE2 (hACE2) receptor. Solid-phase enzyme immunoassays and cell binding assays allow qualitative assessment of binding but lack quantitative evaluation of affinity. Surface plasmon resonance, Bio-layer interferometry, and Microscale Thermophoresis on the other hand, provide accurate affinity measurement through equilibrium dissociation constants (KD). In silico modeling predicts affinity through binding structure modeling, protein-protein docking simulations, and binding energy calculations but reveals inconsistent results due to the lack of a standardized approach. Machine learning and deep learning models utilize simulated and experimental protein-protein interaction data to elucidate the critical residues associated with CoV binding affinity to hACE2. Further optimization and standardization of existing approaches for studying binding affinity could aid pandemic preparedness. Specifically, prioritizing surveillance of CoVs that can bind to human receptors stands to mitigate the risk of zoonotic spillover.

[end paper 6]

[begin paper 7]

PMCID = 10247271

Title = Wastewater early warning system for SARS-CoV-2 outbreaks and variants in a Coruña, Spain

Wastewater-based epidemiology has been widely used as a cost-effective method for tracking the COVID-19 pandemic at the community level. Here we describe COVIDBENS, a wastewater surveillance program running from June 2020 to March 2022 in the wastewater treatment plant of Bens in A Coruña (Spain). The main goal of this work was to provide an effective early warning tool based in wastewater epidemiology to help in decision-making at both the social and public health levels. RT-qPCR procedures and Illumina sequencing were used to weekly monitor the viral load and to detect SARS-CoV-2 mutations in wastewater, respectively. In addition, own statistical models were applied to estimate the real number of infected people and the frequency of each emerging variant circulating in the community, which considerable improved the surveillance strategy. Our analysis detected 6 viral load waves in A Coruña with concentrations between 103 and 106 SARS-CoV-2 RNA copies/L. Our system was able to anticipate community outbreaks during the pandemic with 8–36 days in advance with respect to clinical reports and, to detect the emergence of new SARS-CoV-2 variants in A Coruña such as Alpha (B.1.1.7), Delta (B.1.617.2), and Omicron (B.1.1.529 and BA.2) in wastewater with 42, 30, and 27 days, respectively, before the health system did. Data generated here helped local authorities and health managers to give a faster and more efficient response to the pandemic situation, and also allowed important industrial companies to adapt their production to each situation. The wastewater-based epidemiology program developed in our metropolitan area of A Coruña (Spain) during the SARS-CoV-2 pandemic served as a powerful early warning system combining statistical models with mutations and viral load monitoring in wastewater over time.

The online version contains supplementary material available at 10.1007/s11356-023-27877-3.

[end paper 7]

[begin paper 8]

PMCID = 11316817

Title = De novo generation of SARS-CoV-2 antibody CDRH3 with a pre-trained generative large language model

Artificial Intelligence (AI) techniques have made great advances in assisting antibody design. However, antibody design still heavily relies on isolating antigen-specific antibodies from serum, which is a resource-intensive and time-consuming process. To address this issue, we propose a Pre-trained Antibody generative large Language Model (PALM-H3) for the de novo generation of artificial antibodies heavy chain complementarity-determining region 3 (CDRH3) with desired antigen-binding specificity, reducing the reliance on natural antibodies. We also build a high-precision model antigen-antibody binder (A2binder) that pairs antigen epitope sequences with antibody sequences to predict binding specificity and affinity. PALM-H3-generated antibodies exhibit binding ability to SARS-CoV-2 antigens, including the emerging XBB variant, as confirmed through in-silico analysis and in-vitro assays. The in-vitro assays validate that PALM-H3-generated antibodies achieve high binding affinity and potent neutralization capability against spike proteins of SARS-CoV-2 wild-type, Alpha, Delta, and the emerging XBB variant. Meanwhile, A2binder demonstrates exceptional predictive performance on binding specificity for various epitopes and variants. Furthermore, by incorporating the attention mechanism inherent in the Roformer architecture into the PALM-H3 model, we improve its interpretability, providing crucial insights into the fundamental principles of antibody design.

Antibody design still heavily relies on isolating antigen-specific antibodies from serum. Here the authors report a Pre-trained Antibody generative large Language Model (PALM-H3) for the de novo generation of artificial antibodies heavy chain complementarity-determining region 3 with desired antigen-binding specificity.

[end paper 8]

[begin paper 9]

PMCID = 7979453

Title = Docking and in silico toxicity assessment of Arthrospira compounds as potential antiviral agents against SARS-CoV-2

A race is currently being launched as a result of the international health situation. This race aims to find, by various means, weapons to counter the Covid-19 pandemic now widespread on all continents. The aquatic world and in particular that of photosynthetic organisms is regularly highlighted but paradoxically little exploited in view of the tremendous possibilities it offers. Computational tools allow not only to clear the existence and activity of many molecules but also to model their relationships with receptors identified in potential hosts. On a routine basis, our laboratory carries out a research activity on functionalities of molecules derived from algae using in silico tools. We have implemented our skills in algae biology and in modeling, as tests in order to identify molecules expressed by the genus Arthrospira showing an antiviral potential and more particularly anti-SARS-CoV-2. Using consensus docking and redocking with Autodock Vina and SwissDock, we were able to identify several promising molecules from Arthrospira: phycocyanobilin, phycoerythrobilin, phycourobilin, and folic acid. These four compounds showed reliable binding energies comprised between − 6.95 and − 7.45 kcal.mol−1 in Autodock Vina and between − 9.285 and − 10.35 kcal.mol−1 with SwissDock. Toxicity prediction as well as current regulations provided promising arguments for the inclusion of these compounds in further studies to assess their ability to compete with the SARS-CoV-2/ACE2 complex both in vitro and in vivo.

The online version contains supplementary material available at 10.1007/s10811-021-02372-9.

[end paper 9]

[begin paper 10]

PMCID = 7962425

Title = Serologic Cross-Reactivity of SARS-CoV-2 with Endemic and Seasonal Betacoronaviruses

In order to properly understand the spread of SARS-CoV-2 infection and development of humoral immunity, researchers have evaluated the presence of serum antibodies of people worldwide experiencing the pandemic. These studies rely on the use of recombinant proteins from the viral genome in order to identify serum antibodies that recognize SARS-CoV-2 epitopes. Here, we discuss the cross-reactivity potential of SARS-CoV-2 antibodies with the full spike proteins of four other betacoronaviruses that cause disease in humans, MERS-CoV, SARS-CoV, HCoV-OC43, and HCoV-HKU1. Using enzyme-linked immunosorbent assays (ELISAs), we detected the potential cross-reactivity of antibodies against SARS-CoV-2 towards the four other coronaviruses, with the strongest cross-recognition between SARS-CoV-2 and SARS /MERS-CoV antibodies, as expected based on sequence homology of their respective spike proteins. Further analysis of cross-reactivity could provide informative data that could lead to intelligently designed pan-coronavirus therapeutics or vaccines.

The online version contains supplementary material available at 10.1007/s10875-021-00997-6.

[end paper 10]

[begin paper 11]

PMCID = 7797355

Title = ACE-2-interacting Domain of SARS-CoV-2 (AIDS) Peptide Suppresses Inflammation to Reduce Fever and Protect Lungs and Heart in Mice: Implications for COVID-19 Therapy

COVID-19 is an infectious respiratory illness caused by the virus strain severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) and until now, there is no effective therapy against COVID-19. Since SARS-CoV-2 binds to angiotensin-converting enzyme 2 (ACE2) for entering into host cells, to target COVID-19 from therapeutic angle, we engineered a hexapeptide corresponding to the ACE2-interacting domain of SARS-CoV-2 (AIDS) that inhibits the association between receptor-binding domain-containing spike S1 and ACE-2. Accordingly, wild type (wt), but not mutated (m), AIDS peptide inhibited SARS-CoV-2 spike S1-induced activation of NF-κB and expression of IL-6 in human lungs cells. Interestingly, intranasal intoxication of C57/BL6 mice with recombinant SARS-CoV-2 spike S1 led to fever, increase in IL-6 in lungs, infiltration of neutrophils into the lungs, arrhythmias, and impairment in locomotor activities, mimicking some of the important symptoms of COVID-19. However, intranasal treatment with wtAIDS, but not mAIDS, peptide reduced fever, protected lungs, improved heart function, and enhanced locomotor activities in SARS-CoV-2 spike S1-intoxicated mice. Therefore, selective targeting of ACE2-to-SARS-CoV-2 interaction by wtAIDS may be beneficial for COVID-19.

The online version contains supplementary material available at 10.1007/s11481-020-09979-8.

[end paper 11]

[begin paper 12]

PMCID = 11751191

Title = Paying attention to the SARS-CoV-2 dialect : a deep neural network approach to predicting novel protein mutations

Predicting novel mutations has long-lasting impacts on life science research. Traditionally, this problem is addressed through wet-lab experiments, which are often expensive and time consuming. The recent advancement in neural language models has provided stunning results in modeling and deciphering sequences. In this paper, we propose a Deep Novel Mutation Search (DNMS) method, using deep neural networks, to model protein sequence for mutation prediction. We use SARS-CoV-2 spike protein as the target and use a protein language model to predict novel mutations. Different from existing research which is often limited to mutating the reference sequence for prediction, we propose a parent-child mutation prediction paradigm where a parent sequence is modeled for mutation prediction. Because mutations introduce changing context to the underlying sequence, DNMS models three aspects of the protein sequences: semantic changes, grammatical changes, and attention changes, each modeling protein sequence aspects from shifting of semantics, grammar coherence, and amino-acid interactions in latent space. A ranking approach is proposed to combine all three aspects to capture mutations demonstrating evolving traits, in accordance with real-world SARS-CoV-2 spike protein sequence evolution. DNMS can be adopted for an early warning variant detection system, creating public health awareness of future SARS-CoV-2 mutations.

Elkin and Zhu propose a Deep Novel Mutation Search (DNMS) method, using deep neural networks to model SARS-CoV-2 spike protein sequence for novel mutation prediction, by calculating semantic change, attention change, and grammaticality of an amino acid sequence to rank all possible substitutions.

[end paper 12]

[begin paper 13]

PMCID = 9486763

Title = A novel delayed lateral flow immunoassay for enhanced detection of SARS-CoV-2 spike antigen

A new detection strategy was developed to improve the sensitivity of a lateral flow immunoassay platform utilizing a delayed hydrophobic barrier fabricated with trimethylsilyl cellulose (TMSC). The SARS-CoV-2 spike receptor-binding domain (SARS-CoV-2 SP RBD) antigen was chosen as a model analyte to demonstrate the superior detectability of this scheme. The novel device consists of 2 separate layers, so-called delayed lateral flow immunoassay (d-LFIA). The upper layer is intended for the analyte or sample flow path, where the test solution flows freely straight to the detection zone to bind with the primary antibody. The lower layer, located just underneath, is designed for the SARS-CoV-2 spike receptor-binding domain-conjugated gold nanoparticles (SARS-CoV-2 SP RBD-AuNPs) used for producing a colorimetric signal. This layer is fabricated with a TMSC barrier to time-delay the movement of SARS-CoV-2 SP RBD-AuNPs, thus allowing the antigen to bind with the primary antibody more efficiently. This platform exhibited a 2.6-fold enhancement in the sensitivity and 9.1-fold improvement in the limit of detection (LOD) as compared with the conventional LFIA. In addition, this d-LFIA device was satisfactorily applied to accurate screening of COVID-19 patients.

The online version contains supplementary material available at 10.1007/s00604-022-05467-3.

[end paper 13]

[begin paper 14]

PMCID = 8805427

Title = Variable levels of spike and ORF1ab RNA in post-mortem lung samples of SARS-CoV-2-positive subjects: comparison between ISH and RT-PCR

Post-mortem examination plays a pivotal role in understanding the pathobiology of the SARS-CoV-2; thus, the optimization of virus detection on the post-mortem formalin-fixed paraffin-embedded (FFPE) tissue is needed. Different techniques are available for the identification of the SARS-CoV-2, including reverse transcription polymerase chain reaction (RT-PCR), immunohistochemistry (IHC), in situ hybridization (ISH), and electron microscopy. The main goal of this study is to compare ISH versus RT-PCR to detect SARS-CoV-2 on post-mortem lung samples of positive deceased subjects. A total of 27 samples were analyzed by RT-PCR targeting different viral RNA sequences of SARS-CoV-2, including envelope (E), nucleocapsid (N), spike (S), and open reading frame (ORF1ab) genes and ISH targeting S and Orf1ab. All 27 cases showed the N gene amplification, 22 out of 27 the E gene amplification, 26 out of 27 the S gene amplification, and only 6 the ORF1ab gene amplification. The S ISH was positive only in 12 out of 26 cases positive by RT-PCR. The S ISH positive cases with strong and diffuse staining showed a correlation with low values of the number of the amplification cycles by S RT-PCR suggesting that ISH is a sensitive assay mainly in cases carrying high levels of S RNA. In conclusion, our findings demonstrated that ISH assay has lower sensitivity to detect SARS-CoV-2 in FFPE compared to RT-PCR; however, it is able to localize the virus in the cellular context since it preserves the morphology.

The online version contains supplementary material available at 10.1007/s00428-021-03262-8.

[end paper 14]

[begin paper 15]

PMCID = 7536135

Title = The novel SARS-CoV-2 pandemic: Possible environmental transmission, detection, persistence and fate during wastewater and water treatment

The contagious SARS-CoV-2 virus, responsible for COVID-19 disease, has infected over 27 million people across the globe within a few months. While literature on SARS-CoV-2 indicates that its transmission may occur predominantly via aerosolization of virus-laden droplets, the possibility of alternate routes of transmission and/or reinfection via the environment requires considerable scientific attention. This review aims to collate information on possible transmission routes of this virus, to ascertain its fate in the environment. Concomitant with the presence of SARS-CoV-2 viral RNA in faeces and saliva of infected patients, studies also indicated its occurrence in raw wastewater, primary sludge and river water. Therefore sewerage system could be a possible route of virus outbreak, a possible tool to assess viral community spread and future surveillance technique. Hence, this review looked into detection, occurrence and fate of SARS-CoV-2 during primary, secondary, and tertiary wastewater and water treatment processes based on published literature on SARS-CoV and other enveloped viruses. The review also highlights the need for focused research on occurrence and fate of SARS-CoV-2 in various environmental matrices. Utilization of this information in environmental transmission models developed for other enveloped and enteric viruses can facilitate risk assessment studies. Preliminary research efforts with SARS-CoV-2 and established scientific reports on other coronaviruses indicate that the threat of virus transmission from the aquatic environment may be currently non-existent. However, the presence of viral RNA in wastewater provides an early warning that highlights the need for effective sewage treatment to prevent a future outbreak of SARS-CoV-2.

[end paper 15]

[begin paper 16]

PMCID = 10829978

Title = PandoGen: Generating complete instances of future SARS-CoV-2 sequences using Deep Learning

One of the challenges in a viral pandemic is the emergence of novel variants with different phenotypical characteristics. An ability to forecast future viral individuals at the sequence level enables advance preparation by characterizing the sequences and closing vulnerabilities in current preventative and therapeutic methods. In this article, we explore, in the context of a viral pandemic, the problem of generating complete instances of undiscovered viral protein sequences, which have a high likelihood of being discovered in the future using protein language models. Current approaches to training these models fit model parameters to a known sequence set, which does not suit pandemic forecasting as future sequences differ from known sequences in some respects. To address this, we develop a novel method, called PandoGen, to train protein language models towards the pandemic protein forecasting task. PandoGen combines techniques such as synthetic data generation, conditional sequence generation, and reward-based learning, enabling the model to forecast future sequences, with a high propensity to spread. Applying our method to modeling the SARS-CoV-2 Spike protein sequence, we find empirically that our model forecasts twice as many novel sequences with five times the case counts compared to a model that is 30× larger. Our method forecasts unseen lineages months in advance, whereas models 4× and 30× larger forecast almost no new lineages. When trained on data available up to a month before the onset of important Variants of Concern, our method consistently forecasts sequences belonging to those variants within tight sequence budgets.

Viral protein sequences play a pivotal role in the spread of a pandemic. As the virus evolves, so do the viral proteins, increasing the potency of the virus. Knowledge of future viral protein sequences can be invaluable because it allows us to test the efficacy of preventative and treatment methods against future changes to the virus, and tailor them to such changes early. We attempt to forecast viral proteins ahead of time. Making such predictions is very challenging and complex because the prediction target is a sequence with thousands of positions, and a single mis-predicted sequence position may invalidate the entire prediction. Also, as the virus continues to evolve, the data available to train models becomes obsolete. Addressing these challenges, we create a novel approach to train models of the SARS-CoV-2 Spike protein, that are especially tailored to forecasting future sequences. Models trained using this approach outperform existing approaches in their effectiveness. In addition, our method can train models to forecast important pandemic variants ahead of time.

[end paper 16]

[begin paper 17]

PMCID = 8592829

Title = Comparative structural analyses of selected spike protein-RBD mutations in SARS-CoV-2 lineages

The severity of COVID-19 has been observed throughout the world as severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) globally claimed more than 2 million lives and left a devastating impact worldwide. Recently several virulent mutant strains of this virus, such as the B.1.1.7, B.1.351, and P1 lineages, have emerged with initial predominance in UK, South Africa, and Brazil. Another extremely pathogenic B.1.617 lineage and its sub-lineages, first detected in India, are now affecting some countries at notably stronger spread-rates. The present paper computationally examines the time-based structures of B.1.1.7, B.1.351, and P1 lineages with selected spike protein mutations. The mutations in the more recently found B.1.617 lineage and its sub-lineages are explored, and the implications for multiple point mutations of the spike protein’s receptor-binding domain (RBD) are described. The selected S1 mutations within the highly contagious B.1.617.2 sub-lineage, also known as the delta variant, are examined as well.

The online version contains supplementary material available at 10.1007/s12026-021-09250-z.

[end paper 17]

[begin paper 18]

PMCID = 11161772

Title = Biophysical principles predict fitness of SARS-CoV-2 variants

This research presents a biophysical model that maps the molecular properties of SARS-CoV-2’s receptor binding domain into an epistatic fitness landscape. By linking the binding affinities of the virus to its epidemic fitness, we offer a powerful tool for understanding and predicting the emergence and success of new viral variants. Our model, validated with real-world data and informed by theoretical insights, provides a foundation for interpreting the evolutionary trajectory of past pandemics and predicting those of the future. The adaptability of this biophysical model extends to the key proteins of other viruses as well, signifying its potential in guiding public health interventions, and advancing our understanding of viral evolution.

SARS-CoV-2 employs its spike protein’s receptor binding domain (RBD) to enter host cells. The RBD is constantly subjected to immune responses, while requiring efficient binding to host cell receptors for successful infection. However, our understanding of how RBD’s biophysical properties contribute to SARS-CoV-2’s epidemiological fitness remains largely incomplete. Through a comprehensive approach, comprising large-scale sequence analysis of SARS-CoV-2 variants and the identification of a fitness function based on binding thermodynamics, we unravel the relationship between the biophysical properties of RBD variants and their contribution to viral fitness. We developed a biophysical model that uses statistical mechanics to map the molecular phenotype space, characterized by dissociation constants of RBD to ACE2, LY-CoV016, LY-CoV555, REGN10987, and S309, onto an epistatic fitness landscape. We validate our findings through experimentally measured and machine learning (ML) estimated binding affinities, coupled with infectivity data derived from population-level sequencing. Our analysis reveals that this model effectively predicts the fitness of novel RBD variants and can account for the epistatic interactions among mutations, including explaining the later reversal of Q493R. Our study sheds light on the impact of specific mutations on viral fitness and delivers a tool for predicting the future epidemiological trajectory of previously unseen or emerging low-frequency variants. These insights offer not only greater understanding of viral evolution but also potentially aid in guiding public health decisions in the battle against COVID-19 and future pandemics.

[end paper 18]

[begin paper 19]

PMCID = 8505113

Title = Data-independent acquisition mass spectrometry for site-specific glycoproteomics characterization of SARS-CoV-2 spike protein

The spike protein of SARS-CoV-2, the virus responsible for the global pandemic of COVID-19, is an abundant, heavily glycosylated surface protein that plays a key role in receptor binding and host cell fusion, and is the focus of all current vaccine development efforts. Variants of concern are now circulating worldwide that exhibit mutations in the spike protein. Protein sequence and glycosylation variations of the spike may affect viral fitness, antigenicity, and immune evasion. Global surveillance of the virus currently involves genome sequencing, but tracking emerging variants should include quantitative measurement of changes in site-specific glycosylation as well. In this work, we used data-dependent acquisition (DDA) and data-independent acquisition (DIA) mass spectrometry to quantitatively characterize the five N-linked glycosylation sites of the glycoprotein standard alpha-1-acid glycoprotein (AGP), as well as the 22 sites of the SARS-CoV-2 spike protein. We found that DIA compared favorably to DDA in sensitivity, resulting in more assignments of low-abundance glycopeptides. However, the reproducibility across replicates of DIA-identified glycopeptides was lower than that of DDA, possibly due to the difficulty of reliably assigning low-abundance glycopeptides confidently. The differences in the data acquired between the two methods suggest that DIA outperforms DDA in terms of glycoprotein coverage but that overall performance is a balance of sensitivity, selectivity, and statistical confidence in glycoproteomics. We assert that these analytical and bioinformatics methods for assigning and quantifying glycoforms would benefit the process of tracking viral variants as well as for vaccine development.

The online version contains supplementary material available at 10.1007/s00216-021-03643-7.

[end paper 19]

[begin paper 20]

PMCID = 8286882

Title = Rapid, label-free, and sensitive point-of-care testing of anti-SARS-CoV-2 IgM/IgG using all-fiber Fresnel reflection microfluidic biosensor

The ongoing global pandemic of SARS-CoV-2 has promoted to develop novel serological testing technologies since they can be effectively complementary to RT-PCR. Here, a new all-fiber Fresnel reflection microfluidic biosensor (FRMB) was constructed through combining all-fiber optical system, microfluidic chip, and multimode fiber bio-probe. The transmission of the incident light and the collection and transmission of Fresnel reflection light are achieved using a single-multi-mode fiber optic coupler (SMFC) without any other optical separation elements. This compact design greatly simplifies the whole system structure and improves light transmission efficiency, which makes it suitable for the label-free, sensitive, and easy-to-use point-of-care testing (POCT) of targets in nanoliter samples. Based on Fresnel reflection mechanism and immunoassay principle, both the SARS-CoV-2 IgM and IgG antibodies against the SARS-CoV-2 spike protein could be sensitively quantified in 7 min using the secondary antibodies-modified multimode fiber bio-probe. The FRMB performs in one-step, is accurate, label-free, and sensitive in situ/on-site detection of SARS-CoV-2 IgM or IgG in serum with simple dilution only. The limits of detection of SARS-CoV-2 IgM and SARS-CoV-2 IgG were 0.82 ng/mL and 0.45 ng/mL, respectively. Based on our proposed theory, the affinity constants of SARS-CoV-2 IgM or IgG antibody and their respective secondary antibodies were also determined. The FRMB can be readily extended as a universal platform for the label-free, rapid, and sensitive in situ/on-site measurement of other biomarkers and the investigation of biomolecular interaction.

The online version contains supplementary material available at 10.1007/s00604-021-04911-0.

[end paper 20]

[begin paper 21]

PMCID = 8033097

Title = The percentages of SARS-CoV-2 protein similarity and identity with SARS-CoV and BatCoV RaTG13 proteins can be used as indicators of virus origin

There are three types of proteins in coronaviruses: nonstructural, structural, and accessory proteins. Coronavirus proteins are essential for viral replication and for the binding and invasion of hosts and the regulation of host cell metabolism and immunity. This study investigated the amino acid sequence similarity and identity percentages of 10 proteins in SARS-CoV-2, SARS-CoV and the Rhinolophus affinis bat coronavirus (BatCoV RaTG13). The investigated proteins were the 1ab polyprotein, spike protein, orf3a, the envelope protein, the membrane protein, orf6, orf7a, orf7b, orf8, and the nucleocapsid protein. The online sequence alignment service of The European Molecular Biology Open Software Suite (EMBOSS) was used to determine the percentages of protein similarity and identity in the three viruses. The results showed that the similarity and identity percentages of the SARS-CoV-2 and BatCoV RaTG13 proteins were both greater than 95%, while the identity and similarity percentages of SARS-CoV-2 and SARS-CoV were both greater than 38%. The proteins of SARS-CoV-2 and BatCoV RaTG13 have high identity and similarity compared to those of SARS-CoV-2 and SARS-CoV.

The proteins of the SARS-CoV-2 are most identical and similar to those of BatCoV RaTG13 than to the proteins of SARS-CoV

The online version contains supplementary material available at 10.1007/s42485-021-00060-3.

[end paper 21]

[begin paper 22]

PMCID = 7921825

Title = Electrochemical immunosensor with Cu2O nanocube coating for detection of SARS-CoV-2 spike protein

Severe acute respiratory syndrome SARS-CoV-2 has caused a global pandemic starting in 2020. Accordingly, testing is crucial for mitigating the economic and public health effects. In order to facilitate point-of-care diagnosis, this study aims at presenting a label-free electrochemical biosensor as a powerful nanobiodevice for SARS-CoV-2 spike protein detection. Utilizing the IgG anti-SARS-CoV-2 spike antibody onto the electrode surface as a specific platform in an ordered orientation through staphylococcal protein A (ProtA) is highly significant in fabricating the designed nanobiodevice. In this sense, the screen-printed carbon electrode modified with Cu2O nanocubes (Cu2O NCs), which provide a large surface area in a very small space, was applied in order to increase the ProtA loading on the electrode surface. Accordingly, the sensitivity and stability of the sensing platform significantly increased. The electrochemical evaluations proved that there is a very good linear relationship between the charge transfer resistance (Rct) and spike protein contents via a specific binding reaction in the range 0.25 fg mL−1 to 1 μg mL−1. Moreover, the assay when tested with influenza viruses 1 and 2 was performed in 20 min with a low detection limit of 0.04 fg mL−1 for spike protein without any cross-reactivity. The designed nanobiodevice exhibited an average satisfactory recovery rate of ~ 97–103% in different artificial sample matrices, i.e., saliva, artificial nasal, and universal transport medium (UTM), illustrating its high detection performance and practicability. The nanobiodevice was also tested using real patients and healthy samples, where the results had been already obtained using the standard polymerase chain reaction (PCR) procedure, and showed satisfactory results.

Graphical abstract

The online version contains supplementary material available at 10.1007/s00604-021-04762-9.

[end paper 22]

[begin paper 23]

PMCID = 10124706

Title = A COVID-19 vaccine candidate based on SARS-CoV-2 spike protein and immune-stimulating complexes

Spike protein from SARS-CoV-2, the etiologic agent of the COVID-19 pandemic disease, constitutes a structural protein that proved to be the main responsible for neutralizing antibody production. Thus, its sequence is highly considered for the design of candidate vaccines. Animal cell culture represents the best option for the production of subunit vaccines based on recombinant proteins since they introduce post-translational modifications that are important to mimic the natural antigenic epitopes. Particularly, the human cell line HEK293T has been explored and used for the production of biotherapeutics since the products derived from them present human-like post-translational modifications that are important for the protein’s activity and immunogenicity. The aim of this study was to produce and characterize a potential vaccine for COVID-19 based on the spike ectodomain (S-ED) of SARS-CoV-2 and two different adjuvants: aluminum hydroxide (AH) and immune-stimulating complexes (ISCOMs). The S-ED was produced in sHEK293T cells using a 1-L stirred tank bioreactor operated in perfusion mode and purified. S-ED characterization revealed the expected size and morphology. High N-glycan content was confirmed. S-ED-specific binding with the hACE2 (human angiotensin-converting enzyme 2) receptor was verified. The immunogenicity of S-ED was evaluated using AH and ISCOMs. Both formulations demonstrated the presence of anti-RBD antibodies in the plasma of immunized mice, being significantly higher for the latter adjuvant. Also, higher levels of IFN-γ and IL-4 were detected after the ex vivo immune stimulation of spleen-derived MNCs from ISCOMs immunized mice. Further analysis confirmed that S-ED/ISCOMs elicit neutralizing antibodies against SARS-CoV-2.

 Trimeric SARS-CoV-2 S-ED was produced in stable recombinant sHEK cells in serum-free medium. 

 A novel S-ED vaccine formulation induced potent humoral and cellular immunity. 

 S-ED formulated with ISCOMs adjuvant elicited a highly neutralizing antibody titer. 

The online version contains supplementary material available at 10.1007/s00253-023-12520-5.

[end paper 23]

[begin paper 24]

PMCID = 10458003

Title = Dynamic Evolution of SARS-CoV-2 in a Patient on Chemotherapy

Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) has evolved significantly during the pandemic and resulted in daunting numbers of genomic sequences. Tracking SARS-CoV-2 evolution during persistent cases could provide insight into the origins and dynamics of new variants. We report here a case of B-cell acute lymphocytic leukemia on chemotherapy with infection of SARS-CoV-2 for more than two months. Genomic surveillance of his serial SARS-CoV-2-positive specimens revealed two unprecedented large deletions, Δ15–26 and Δ138–145, in the viral spike protein N-terminal domain (NTD) and demonstrated their dynamic shifts in generating these new variants. Located at antigenic supersites, these large deletions are anticipated to dramatically change the spike protein NTD in three-dimensional protein structure prediction, which may lead to immune escape but reduce their viral transmissibility. In summary, we present here a new viral evolutionary trajectory in a patient on chemotherapy.

[end paper 24]

[begin paper 25]

PMCID = 8628143

Title = SARS-CoV-2 Neutralization in Convalescent Plasma and Commercial Lots of Plasma-Derived Immunoglobulin

Patients with primary or secondary immunodeficiency (PID or SID) face increased insecurity and discomfort in the light of the COVID-19 pandemic, not knowing if and to what extent their comorbidities may impact the course of a potential SARS-CoV-2 infection. Furthermore, recently available vaccination options might not be amenable or effective for all patients in this heterogeneous population. Therefore, these patients often rely on passive immunization with plasma-derived, intravenous or subcutaneous immunoglobulin (IVIG/SCIG).

Whether the ongoing COVID-19 pandemic and/or the progress in vaccination programs lead to increased and potentially protective titers in plasma-derived immunoglobulins (Ig) indicated (e.g., for humoral immunodeficiency) remains a pressing question for this patient population.

We investigated SARS-CoV-2 reactivity of US plasma-derived IVIG/SCIG products from the end of 2020 until June 2021 as well as in convalescent plasma (CP) from May 2020 to August 2020 to determine whether potentially neutralizing antibody titers may be present.

Final containers of IVIG/SCIG and CP donations were analyzed by commercial ELISA for anti-SARS-CoV-2 S1-receptor binding domain (RBD) IgG as well as microneutralization assay using a patient-derived SARS-CoV-2 (D614G) isolate. Neutralization capacities of 313 single plasma donations and 119 plasma-derived IVIG/SCIG lots were determined. Results obtained from both analytical methods were normalized against the WHO International Standard. Finally, based on dense pharmacokinetic profiles of an IVIG preparation from previously published investigations, possible steady-state plasma levels of SARS-CoV-2 neutralization capacities were approximated based on currently measured anti-SARS-CoV-2 potencies in IVIG/SCIG preparations.

CP donations presented with high variability with regards to anti-SARS-CoV-2 reactivity in ELISA as well as in neutralization testing. While approximately 50% of convalescent donations were not/low neutralizing, approximately 10% were at or above 600 IU/mL. IVIG/SCIG lots derived from pre-pandemic plasma donations did not show neutralizing capacities for SARS-CoV-2. Lots produced between December 2020 and June 2021 entailing plasma donations after the emergence of SARS-CoV-2 showed a rapid and constant increase in anti-SARS-CoV-2 reactivity and neutralization capacity over time. While lot-to-lot variability was substantial, neutralization capacity increased from a mean of 21 IU/mL in December 2020 to 506 IU/mL in June 2021 with a maximum of 864 IU/mL for the most recent lots. Pharmacokinetic extrapolations, based on non-compartmental superposition principles using steady-state reference profiles from previously published pharmacokinetic investigations on IVIG in PID, yielded potential steady-state trough plasma levels of 16 IU/mL of neutralizing SARS-CoV-2 IgG based on the average final container concentration from May 2021 of 216 IU/mL. Maximum extrapolated trough levels could reach 64 IU/mL based on the latest maximal final container potency tested in June 2021.

SARS-CoV-2 reactivity and neutralization capacity in IVIG/SCIG produced from US plasma rapidly and in part exponentially increased in the first half of 2021. The observed increase of final container potencies is likely trailing the serological status of the US donor population in terms of COVID-19 convalescence and vaccination by at least 5 months due to production lead times and should in principle continue at least until Fall 2021. In summary, the data support rapidly increasing levels of anti-SARS-CoV-2 antibodies in IVIG/SCIG products, implicating that a certain level of protection could be possible against COVID-19 for regularly substituted PID/SID patients. Nevertheless, more research is still needed to confirm which plasma levels are needed to provide protection against SARS-CoV-2 infection in immune-compromised patients.

The online version contains supplementary material available at 10.1007/s40259-021-00511-9.

People with deficiencies in their immune system often have an insufficient antibody response to antigens such as bacteria, viruses, or vaccines. These patients therefore often receive antibodies from healthy people to replace the missing antibodies and build a first line of defense against infections. These antibodies (also called immunoglobulins [Ig]) are prepared from plasma, the liquid fraction of the blood without cells, of healthy donors. This plasma is then split up during pharmaceutical production into its protein components. One of these is immunoglobulin G (IgG), which is the protein family that neutralizes/inactivates infectious agents as well as marks these infectious agents so they can be recognized by other parts of the immune system. With the ongoing COVID-19 pandemic and the severe to fatal outcomes for certain patient groups, especially people with impaired immunity, these patients and their physicians are interested in whether their antibody replacement therapy also confers protection against SARS-CoV-2 infection. We analyzed the capability of plasma-derived Ig lots to (i) recognize SARS-CoV-2 protein by ELISA method as well as (ii) neutralize SARS-CoV-2 by neutralization studies using the actual virus under biosafety level 3 (BSL-3) conditions. Here we show increasing anti-SARS-CoV-2 activity over time of manufactured Ig lots produced between December 2020 and June 2021. The most recent lots had a neutralizing activity of up to 864 IU/mL. Considering that the US represents Octapharma’s main plasma source, the progress in vaccination levels together with the evolution of the COVID-19 pandemic in this country suggests that the intravenous or subcutaneous immunoglobulin (IVIG/SCIG) neutralization capacities against SARS-CoV-2 might still increase and could potentially reach a level where antibody plasma concentrations in the patient confer immune protection.

The online version contains supplementary material available at 10.1007/s40259-021-00511-9.

[end paper 25]

[begin paper 26]

PMCID = 7895511

Title = Screening and evaluation of anti-SARS-CoV-2 components from Ephedra sinica by ACE2/CMC-HPLC-IT-TOF-MS approach

Traditional Chinese medicines played an important role in the treatment of COVID-19 in 2020. Ephedra sinica, one of the major constituent herbs of multi-component herbal formula, has been widely used to treat COVID-19 in China. However, its active components are still unclear. The objectives of this study are to screen and evaluate active components from the traditional Chinese medicine Ephedra sinica for the treatment of COVID-19. In our study, we established an ACE2/CMC bioaffinity chromatography model, and then developed an ACE2/CMC-HPLC-IT-TOF-MS system for the active compounds screening and identification from Ephedra sinica extract. We performed molecular docking and surface plasmon resonance (SPR) assays to assess the binding characteristics (binding mode and KD value). We used CCK-8 staining to assess the toxicity of screened compounds, and also used SARS-CoV-2 pseudovirus to observe the viropexis effect of screened compounds in ACE2h cells. In this current work, one fraction was fished out, separated and identified as ephedrine (EP), pseudoephedrine (PEP), and methylephedrine (MEP). Binding assays showed that the three compounds could bind with ACE2 in a special way to some amino acid residues, similar to the way SARS-CoV-2 bound with ACE2. Additionally, the three compounds, especially EP, can inhibit the entrance of SARS-CoV-2 spike pseudovirus into ACE2h cells because they can reduce the entrance ratio of pseudovirus in the pseudovirus model. Overall, the ACE2/CMC-HPLC-IT-TOF-MS system was established and verified to be suitable for ACE2-targeted bioactive compound screening. EP, PEP, and MEP with ACE2-binding features were screened out from Ephedra sinica, and acted as blockers inhibiting SARS-CoV-2 spike pseudovirus entering ACE2h cells.

The online version contains supplementary material available at 10.1007/s00216-021-03233-7.

[end paper 26]

[begin paper 27]

PMCID = 8279807

Title = Phytocompounds of Rheum emodi, Thymus serpyllum, and Artemisia annua Inhibit Spike Protein of SARS-CoV-2 Binding to ACE2 Receptor: In Silico Approach

COVID-19, the disease caused by SARS-CoV-2, has been declared as a global pandemic. Traditional medicinal plants have long history to treat viral infections. Our in silico approach suggested that unique phytocompounds such as emodin, thymol and carvacrol, and artemisinin could physically bind SARS-CoV-2 spike glycoproteins (6VXX and 6VYB), SARS-CoV-2 B.1.351 South Africa variant of Spike glycoprotein (7NXA), and even with ACE2 and prevent the SARS-CoV-2 binding to the host ACE2, TMPRSS2 and neutrapilin-1 receptors. Since Chloroquine has been looked as potential therapy against COVID-19, we also compared the binding of chloroquine and artemisinin for its interaction with spike proteins (6VXX, 6VYB) and its variant 7NXA, respectively. Molecular docking study of phytocompounds and SARS-CoV-2 spike protein was performed by using AutoDock/Vina software. Molecular dynamics (MD) simulation was performed for 50ns. Among all the phytocompounds, molecular docking studies revealed lowest binding energy of artemisinin with 6VXX and 6VYB, with Etotal −10.5 KJ mol−1 and −10.3 KJ mol−1 respectively. Emodin showed the best binding affinity with 6VYB with Etotal −8.8 KJ mol−1and SARS-CoV-2 B.1.351 variant (7NXA) with binding energy of −6.4KJ mol−1. Emodin showed best interactions with TMPRSS 2 and ACE2 with Etotal of −7.1 and −7.3 KJ mol−1 respectively, whereas artemisinin interacts with TMPRSS 2 and ACE2 with Etotal of −6.9 and −7.4 KJ mol−1 respectively. All the phytocompounds were non-toxic and non-carcinogenic. MD simulation showed that artemisinin has more stable interaction with 6VYB as compared to 6VXX, and hence proposed as potential phytochemical to prevent SARS-CoV-2 interaction with ACE-2 receptor.

The online version contains supplementary material available at 10.1007/s40495-021-00259-4.

[end paper 27]

[begin paper 28]

PMCID = 8289455

Title = Ultrasensitive, high-throughput, and rapid simultaneous detection of SARS-CoV-2 antigens and IgG/IgM antibodies within 10 min through an immunoassay biochip

COVID-19 is now a severe threat to global health. Facing this pandemic, we developed a space-encoding microfluidic biochip for high-throughput, rapid, sensitive, simultaneous quantitative detection of SARS-CoV-2 antigen proteins and IgG/IgM antibodies in serum. The proposed immunoassay biochip integrates the advantages of graphene oxide quantum dots (GOQDs) and microfluidic chip and is capable of conducting multiple SARS-CoV-2 antigens or IgG/IgM antibodies of 60 serum samples simultaneously with only 2 μL sample volume of each patient. Fluorescence intensity of antigens and IgG antibody detection at emission wavelength of ~680 nm was used to quantify the target concentration at excitation wavelength of 632 nm, and emission wavelength of ~519 nm was used during the detection of IgM antibodies at excitation wavelength of 488 nm. The method developed has a large linear quantification detection regime of 5 orders of magnitude, an ultralow detection limit of ~0.3 pg/mL under optimized conditions, and less than 10-min qualitative detection time. The proposed biosensing platform will not only greatly facilitate the rapid diagnosis of COVID-19 patients, but also provide a valuable screening approach for infected patients, medical therapy, and vaccine recipients.

The online version contains supplementary material available at 10.1007/s00604-021-04896-w.

[end paper 28]

[begin paper 29]

PMCID = 9016216

Title = MicroRNAs as the Potential Regulators of SARS-CoV-2 Infection and Modifiers of the COVID-19 Clinical Features

The pandemic of coronavirus disease 2019 (COVID-19) warrants the identification of factors that may determine both risk and severity of infection. The factors include microRNAs that have a wide regulatory potential and hence are particularly interesting. The review focuses on the potential roles of human microRNAs and the viral genome as well as microRNAs in SARS-CoV-2 infection and clinical features of COVID-19. The review summarizes the information about the human microRNAs that are thought to specifically bind to the SARS-CoV-2 genome and considers their expression levels in various organs (cells) in both healthy state and pathologies that are risk factors for severe COVID-19. Potential mechanisms whereby SARS-CoV-2 may affect the clinical features of COVID-19 are discussed in brief. The mechanisms include blocking of human microRNAs and RNA-binding proteins, changes in gene expression in infected cells, and possible epigenetic modifications of the human genome with the participation of coronavirus microRNAs.

The online version contains supplementary material available at 10.1134/S0026893322010034.

[end paper 29]

[begin paper 30]

PMCID = 7509052

Title = Insights into the biased activity of dextromethorphan and haloperidol towards SARS-CoV-2 NSP6: in silico binding mechanistic analysis

The outbreak of novel coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) virus continually led to infect a large population worldwide. SARS-CoV-2 utilizes its NSP6 and Orf9c proteins to interact with sigma receptors that are implicated in lipid remodeling and ER stress response, to infect cells. The drugs targeting the sigma receptors, sigma-1 and sigma-2, have emerged as effective candidates to reduce viral infectivity, and some of them are in clinical trials against COVID-19. The antipsychotic drug, haloperidol, exerts remarkable antiviral activity, but, at the same time, the sigma-1 benzomorphan agonist, dextromethorphan, showed pro-viral activity. To explore the potential mechanisms of biased binding and activity of the two drugs, haloperidol and dextromethorphan towards NSP6, we herein utilized molecular docking–based molecular dynamics simulation studies. Our extensive analysis of the protein-drug interactions, structural and conformational dynamics, residual frustrations, and molecular switches of NSP6-drug complexes indicates that dextromethorphan binding leads to structural destabilization and increase in conformational dynamics and energetic frustrations. On the other hand, the strong binding of haloperidol leads to minimal structural and dynamical perturbations to NSP6. Thus, the structural insights of stronger binding affinity and favorable molecular interactions of haloperidol towards viral NSP6 suggests that haloperidol can be potentially explored as a candidate drug against COVID-19.

•Inhibitors of sigma receptors are considered as potent drugs against COVID-19.

•Antipsychotic drug, haloperidol, binds strongly to NSP6 and induces the minimal changes in structure and dynamics of NSP6.

•Dextromethorphan, agonist of sigma receptors, binding leads to overall destabilization of NSP6.

•These two drugs bind with NSP6 differently and also induce differences in the structural and conformational changes that explain their different mechanisms of action.

•Haloperidol can be explored as a candidate drug against COVID-19.

The online version of this article (10.1007/s00109-020-01980-1) contains supplementary material, which is available to authorized users.

[end paper 30]

[begin paper 31]

PMCID = 10032659

Title = Pathogenic mechanisms of post-acute sequelae of SARS-CoV-2 infection (PASC)

COVID-19, with persistent and new onset of symptoms such as fatigue, post-exertional malaise, and cognitive dysfunction that last for months and impact everyday functioning, is referred to as Long COVID under the general category of post-acute sequelae of SARS-CoV-2 infection (PASC). PASC is highly heterogenous and may be associated with multisystem tissue damage/dysfunction including acute encephalitis, cardiopulmonary syndromes, fibrosis, hepatobiliary damages, gastrointestinal dysregulation, myocardial infarction, neuromuscular syndromes, neuropsychiatric disorders, pulmonary damage, renal failure, stroke, and vascular endothelial dysregulation. A better understanding of the pathophysiologic mechanisms underlying PASC is essential to guide prevention and treatment. This review addresses potential mechanisms and hypotheses that connect SARS-CoV-2 infection to long-term health consequences. Comparisons between PASC and other virus-initiated chronic syndromes such as myalgic encephalomyelitis/chronic fatigue syndrome and postural orthostatic tachycardia syndrome will be addressed. Aligning symptoms with other chronic syndromes and identifying potentially regulated common underlining pathways may be necessary for understanding the true nature of PASC. The discussed contributors to PASC symptoms include sequelae from acute SARS-CoV-2 injury to one or more organs, persistent reservoirs of the replicating virus or its remnants in several tissues, re-activation of latent pathogens such as Epstein–Barr and herpes viruses in COVID-19 immune-dysregulated tissue environment, SARS-CoV-2 interactions with host microbiome/virome communities, clotting/coagulation dysregulation, dysfunctional brainstem/vagus nerve signaling, dysautonomia or autonomic dysfunction, ongoing activity of primed immune cells, and autoimmunity due to molecular mimicry between pathogen and host proteins. The individualized nature of PASC symptoms suggests that different therapeutic approaches may be required to best manage specific patients.

[end paper 31]

[begin paper 32]

PMCID = 10362000

Title = Identification and validation of fusidic acid and flufenamic acid as inhibitors of SARS-CoV-2 replication using DrugSolver CavitomiX

In this work, we present DrugSolver CavitomiX, a novel computational pipeline for drug repurposing and identifying ligands and inhibitors of target enzymes. The pipeline is based on cavity point clouds representing physico-chemical properties of the cavity induced solely by the protein. To test the pipeline’s ability to identify inhibitors, we chose enzymes essential for SARS-CoV-2 replication as a test system. The active-site cavities of the viral enzymes main protease (Mpro) and papain-like protease (Plpro), as well as of the human transmembrane serine protease 2 (TMPRSS2), were selected as target cavities. Using active-site point-cloud comparisons, it was possible to identify two compounds—flufenamic acid and fusidic acid—which show strong inhibition of viral replication. The complexes from which fusidic acid and flufenamic acid were derived would not have been identified using classical sequence- and structure-based methods as they show very little structural (TM-score: 0.1 and 0.09, respectively) and very low sequence (~ 5%) identity to Mpro and TMPRSS2, respectively. Furthermore, a cavity-based off-target screening was performed using acetylcholinesterase (AChE) as an example. Using cavity comparisons, the human carboxylesterase was successfully identified, which is a described off-target for AChE inhibitors.

[end paper 32]

[begin paper 33]

PMCID = 7856849

Title = Sensitivity of anti-SARS-CoV-2 serological assays in a high-prevalence setting

Evaluation and power of seroprevalence studies depend on the performed serological assays. The aim of this study was to assess four commercial serological tests from EUROIMMUN, DiaSorin, Abbott, and Roche as well as an in-house immunofluorescence and neutralization test for their capability to identify SARS-CoV-2 seropositive individuals in a high-prevalence setting. Therefore, 42 social and working contacts of a German super-spreader were tested. Consistent with a high-prevalence setting, 26 of 42 were SARS-CoV-2 seropositive by neutralization test (NT), and immunofluorescence test (IFT) confirmed 23 of these 26 positive test results (NT 61.9% and IFT 54.8% seroprevalence). Four commercial assays detected anti-SARS-CoV-2 antibodies in 33.3-40.5% individuals. Besides an overall discrepancy between the NT and the commercial assays regarding their sensitivity, this study revealed that commercial SARS-CoV-2 spike-based assays are better to predict the neutralization titer than nucleoprotein-based assays are.

The online version contains supplementary material available at 10.1007/s10096-021-04169-7.

[end paper 33]

[begin paper 34]

PMCID = 10052277

Title = Detection of SARS-CoV-2 receptor binding domain using fluorescence probe and DNA flowers enabled by rolling circle amplification

Using rolling circle amplification (RCA) and two different ways of signal readout, we developed analytical methods to detect the receptor-binding domain (RBD) of SARS-CoV-2 spike protein (S protein). We modified streptavidin-coated magnetic beads with an aptamer of RBD through a biotin-tagged complementary DNA strand (biotin-cDNA). Binding of RBD caused the aptamer to dissociate from the biotin-cDNA, making the cDNA available to initiate RCA on the magnetic beads. Detection of RBD was achieved using a dual signal output. For fluorescence signaling, the RCA products were mixed with a dsDNA probe labeled with fluorophore and quencher. Hybridization of the RCA products caused the dsDNA to separate and to emit fluorescence (λex = 488 nm, λem = 520 nm). To generate easily detectable UV–vis absorbance signal, the RCA amplification was extended to produce DNA flower to encapsulate horseradish peroxidase (HRP). The HRP-encapsulated DNA flower catalyzed a colorimetric reaction between H2O2 and 3,3′,5,5′-tetramethylbenzidine (TMB) to generate an optical signal (λabs = 450 nm). The fluorescence and colorimetric assays for RBD have low detection limits (0.11 pg mL−1 and 0.904 pg mL−1) and a wide linear range (0.001–100 ng mL−1). For detection of RBD in human saliva, the recovery was 93.0–100% for the fluorescence assay and 87.2–107% for the colorimetric assay. By combining fluorescence and colorimetric detection with RCA, detection of the target RBD in human saliva was achieved with high sensitivity and selectivity.

The online version contains supplementary material available at 10.1007/s00604-023-05747-6.

[end paper 34]

[begin paper 35]

PMCID = 8883239

Title = In silico studies on structural inhibition of SARS-CoV-2 main protease Mpro by major secondary metabolites of Andrographis paniculata and Cinchona officinalis

The COVID-19 infection by Novel Corona Virus (SARS-CoV-2) has become one of the largest pandemic diseases, with cumulative confirmed infections of 275,233,892 and 5,364,996 deaths to date according to World Health Organization. Due to the absence of any approved antiviral drug to treat COVID-19, its lethality is getting severe with time. The main protease of SARS-CoV-2, Mpro is considered one of the potential drug targets because of its role in processing proteins translated from viral RNA. In the present study, four of the plant metabolites, 14-deoxy-11,12-didehydroandrographolide, andrograpanin, quinine, cinchonine from two eminent medicinal plants Andrographis paniculata and Cinchona officinalis, have been evaluated against the main protease of SARS-CoV-2 through in-silico molecular docking and molecular dynamics simulation study. From the result interpretations, it is found that andrograpanin has strong binding affinities with the target protein in its active site with potential negative energies. Molecular Dynamic simulation and MMGBSA studies suggest that earlier reported N3 inhibitor and andrograpanin exhibit effective binding interactions involving identical amino acid residues with the same binding pockets of the main protease of SARS-CoV-2. Therefore, the theoretical experiment suggests that andrograpanin, could be considered the promising inhibitor against SARS-CoV-2 Mpro.

The online version contains supplementary material available at 10.1007/s11756-022-01012-y.

[end paper 35]

[begin paper 36]

PMCID = 8383918

Title = A rapid and reliable liquid chromatography/mass spectrometry method for SARS-CoV-2 analysis from gargle solutions and saliva

We describe a rapid liquid chromatography/tandem mass spectrometry (LC-MS/MS) method for the direct detection and quantitation of SARS-CoV-2 nucleoprotein in gargle solutions and saliva. The method is based on a multiple-reaction monitoring (MRM) mass spectrometry approach with a total cycle time of 5 min per analysis and allows the detection and accurate quantitation of SARS-CoV-2 nucleoprotein as low as 500 amol/μL. We improved the sample preparation protocol of our recent piloting SARS-CoV-2 LC-MS study regarding sensitivity, reproducibility, and compatibility with a complementary reverse transcriptase quantitative polymerase chain reaction (RT-qPCR) analysis of the same sample. The aim of this work is to promote diagnostic tools that allow identifying and monitoring SARS-CoV-2 infections by LC-MS/MS methods in a routine clinical environment.

The online version contains supplementary material available at 10.1007/s00216-021-03614-y.

[end paper 36]

[begin paper 37]

PMCID = 11601794

Title = Rapid response to fast viral evolution using AlphaFold 3-assisted topological deep learning

The fast evolution of SARS-CoV-2 and other infectious viruses poses a grand challenge to the rapid response in terms of viral tracking, diagnostics, and design and manufacture of monoclonal antibodies (mAbs) and vaccines, which are both time-consuming and costly. This underscores the need for efficient computational approaches. Recent advancements, like topological deep learning (TDL), have introduced powerful tools for forecasting emerging dominant variants, yet they require deep mutational scanning (DMS) of viral surface proteins and associated three-dimensional (3D) protein-protein interaction (PPI) complex structures. We propose an AlphaFold 3 (AF3)-assisted multi-task topological Laplacian (MT-TopLap) strategy to address this need. MT-TopLap combines deep learning with topological data analysis (TDA) models, such as persistent Laplacians (PL) to extract detailed topological and geometric characteristics of PPIs, thereby enhancing the prediction of DMS and binding free energy (BFE) changes upon virus mutations. Validation with four experimental DMS datasets of SARS-CoV-2 spike receptor-binding domain (RBD) and the human angiotensin-converting enzyme-2 (ACE2) complexes indicates that our AF3 assisted MT-TopLap strategy maintains robust performance, with only an average 1.1% decrease in Pearson correlation coefficients (PCC) and an average 9.3% increase in root mean square errors (RMSE), compared with the use of experimental structures. Additionally, AF3-assisted MT-TopLap achieved a PCC of 0.81 when tested with a SARS-CoV-2 HK.3 variant DMS dataset, confirming its capability to accurately predict BFE changes and adapt to new experimental data, thereby showcasing its potential for rapid and effective response to fast viral evolution.

[end paper 37]

[begin paper 38]

PMCID = 7603175

Title = In silico Investigation on the Inhibiting Role of Nicotine/Caffeine by Blocking the S Protein of SARS-CoV-2 Versus ACE2 Receptor

In this paper, we studied the in silico interaction of angiotensin-converting enzyme 2 (ACE2) human receptor with two bioactive compounds, i.e., nicotine and caffeine, via molecular dynamic (MD) simulations. The simulations reveal the efficient blocking of ACE2 by caffeine and nicotine in the exposure to the spike (S) protein of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). We have selected the two most important active sites of ACE2-S protein, i.e., 6LZG and 6VW1, which are critically responsible in the interaction of S protein to the receptor and thus, we investigated their interaction with nicotine and caffeine through MD simulations. Caffeine and nicotine are interesting structures for interactions because of their similar structure to the candidate antiviral drugs. Our results reveal that caffeine or nicotine in a specific molar ratio to 6LZG shows a very strong interaction and indicate that caffeine is more efficient in the interaction with 6LZG and further blocking of this site against S protein binding. Further, we investigated the interaction of ACE2 receptor- S protein with nicotine or caffeine when mixed with candidate or approved antiviral drugs for SARS-CoV-2 therapy. Our MD simulations suggest that the combination of caffeine with ribavirin shows a stronger interaction with 6VW1, while in case of favipiravir+nicotine, 6LZG shows potent efficacy of these interaction, proposing the potent efficacy of these combinations for blocking ACE2 receptor against SARS-CoV-2.

[end paper 38]

[begin paper 39]

PMCID = 10261845

Title = Predicting the antigenic evolution of SARS-COV-2 with deep learning

The relentless evolution of SARS-CoV-2 poses a significant threat to public health, as it adapts to immune pressure from vaccines and natural infections. Gaining insights into potential antigenic changes is critical but challenging due to the vast sequence space. Here, we introduce the Machine Learning-guided Antigenic Evolution Prediction (MLAEP), which combines structure modeling, multi-task learning, and genetic algorithms to predict the viral fitness landscape and explore antigenic evolution via in silico directed evolution. By analyzing existing SARS-CoV-2 variants, MLAEP accurately infers variant order along antigenic evolutionary trajectories, correlating with corresponding sampling time. Our approach identified novel mutations in immunocompromised COVID-19 patients and emerging variants like XBB1.5. Additionally, MLAEP predictions were validated through in vitro neutralizing antibody binding assays, demonstrating that the predicted variants exhibited enhanced immune evasion. By profiling existing variants and predicting potential antigenic changes, MLAEP aids in vaccine development and enhances preparedness against future SARS-CoV-2 variants.

SARS-CoV-2’s rapid evolution threatens public health. Here, authors present a deep learning approach to forecast high-risk mutations that may appear in the future, aiding vaccine development and enhancing preparedness against future variants.

[end paper 39]

[begin paper 40]

PMCID = 7779244

Title = Molecular modeling of natural and synthesized inhibitors against SARS-CoV-2 spike glycoprotein

Viral diseases increasingly endanger the world public health because of the transient efficacy of antiviral therapies. The novel coronavirus disease 2019 (COVID-19) has been recently identified as caused by a new type of coronaviruses. This type of coronavirus binds to the human receptor through the Spike glycoprotein (S) Receptor Binding Domain (RBD). The spike protein is found in inaccessible (closed) or accessible (open) conformations in which the accessible conformation causes severe infection. Thus, this receptor is a significant target for antiviral drug design.

An attempt was made to recognize 111 natural and synthesized compounds in order to utilize them against SARS-CoV-2 spike glycoprotein to inhibit Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) using simulation methods, such as molecular docking. The FAF-Drugs3, Pan-Assay Interference Compounds (PAINS), ADME (absorption, distribution, metabolism, excretion) databases along with Lipinski’s rules were used to evaluate the drug-like properties of the identified ligands. In order to analyze and identify the residues critical in the docking process of the spike glycoprotein, the interactions of proposed ligands with both conformations of the spike glycoprotein was simulated.

The results showed that among the available ligands, seven ligands had significant interactions with the binding site of the spike glycoprotein, in which angiotensin-converting enzyme 2 (ACE2) is bounded. Out of seven candidate molecules, six ligands exhibited drug-like characteristics. The results also demonstrated that fluorophenyl and propane groups of ligands had optimal interactions with the binding site of the spike glycoprotein.

According to the results, our findings indicated the ability of six ligands to prevent the binding of the SARS-CoV-2 spike glycoprotein to its cognate receptor, providing novel compounds for the treatment of COVID-19.

The online version contains supplementary material available at 10.1007/s42600-020-00122-3.

[end paper 40]

[begin paper 41]

PMCID = 8216326

Title = Simultaneous enrichment and separation of neutral and sialyl glycopeptides of SARS-CoV-2 spike protein enabled by dual-functionalized Ti-IMAC material

The coronavirus disease 2019 (COVID-19) pandemic caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) presents a serious threat to human health all over the world. The development of effective vaccines has been focusing on the spike (S) glycoprotein, which mediates viral invasion to human cells through its interaction with the angiotensin-converting enzyme 2 (ACE2) receptor. In this work, we perform analytical characterization of N- and O-linked glycosylation of the SARS-CoV-2 S glycoprotein. We explore the novel use of dual-functionalized titanium (IV)-immobilized metal affinity chromatography (Ti-IMAC) material for simultaneous enrichment and separation of neutral and sialyl glycopeptides of a recombinant SARS-CoV-2 S glycoprotein from HEK293 cells. This strategy helps eliminate signal suppression from neutral glycopeptides for the detection of sialyl glycopeptides and improves the glycoform coverage of the S protein. We profiled 19 of its 22 potential N-glycosylated sites with 398 unique glycoforms using the dual-functional Ti-IMAC approach, which exhibited improvement of coverage by 1.6-fold compared to the conventional hydrophilic interaction chromatography (HILIC) glycopeptide enrichment method. We also identified O-linked glycosylation site that was not found using the conventional HILIC approach. In addition, we reported on the identification of mannose-6-phosphate (M6P) glycosylation, which substantially expands the current knowledge of the spike protein’s glycosylation landscape and enables future investigation into the influence of M6P glycosylation of the spike protein on its cell entry.

The online version contains supplementary material available at 10.1007/s00216-021-03433-1.

[end paper 41]

[begin paper 42]

PMCID = 8402008

Title = The Anti-Viral Applications of Marine Resources for COVID-19 Treatment: An Overview

The ongoing pandemic has led to an urgent need for novel drug discovery and potential therapeutics for Sars-CoV-2 infected patients. Although Remdesivir and the anti-inflammatory agent dexamethasone are currently on the market for treatment, Remdesivir lacks full efficacy and thus, more drugs are needed. This review was conducted through literature search of PubMed, MDPI, Google Scholar and Scopus. Upon review of existing literature, it is evident that marine organisms harbor numerous active metabolites with anti-viral properties that serve as potential leads for COVID-19 therapy. Inorganic polyphosphates (polyP) naturally found in marine bacteria and sponges have been shown to prevent viral entry, induce the innate immune response, and downregulate human ACE-2. Furthermore, several marine metabolites isolated from diverse sponges and algae have been shown to inhibit main protease (Mpro), a crucial protein required for the viral life cycle. Sulfated polysaccharides have also been shown to have potent anti-viral effects due to their anionic properties and high molecular weight. Likewise, select marine sponges produce bromotyrosines which have been shown to prevent viral entry, replication and protein synthesis. The numerous compounds isolated from marine resources demonstrate significant potential against COVID-19. The present review for the first time highlights marine bioactive compounds, their sources, and their anti-viral mechanisms of action, with a focus on potential COVID-19 treatment. 

[end paper 42]

[begin paper 43]

PMCID = 10811151

Title = Seroprevalence of anti-SARS-CoV-2 antibodies in household domestic ferrets (Mustela putorius furo) in Spain, 2019–2023

SARS-CoV-2 is the causal agent of Coronavirus Disease 2019 (COVID-19) in humans that emerged in late 2019. This virus is able to infect humans and different animal species. Among pets, cats and ferrets are more susceptible to be infected by the SARS-CoV-2. Epidemiological studies are an important tool to provide information under natural conditions of exposure to SARS-CoV-2 virus. In comparison to cats, limited epidemiological studies have been performed in domestic ferrets (Mustela putorius furo) reporting the presence of antibodies in this species. This study analysed the presence of anti-SARS-CoV-2 antibodies in 432 cliend-owned ferrets from different geographical areas of Spain during the different waves of COVID-19 outbreaks from December 2019 to May 2023 (42 months). For this purpose, anti-SARS-CoV-2 antibodies were detected by an enzyme-linked immunosorbent method (ELISA) using the receptor binding domain (RBD) of Spike antigen and confirmed by serum virus neutralization assay. Eighteen of the 432 ferrets included were seroreactive by the in-house ELISA (4.17%, 95% Confidence Interval (CI): 2.65–6.49). In this sense, the wave of COVID-19 with the higher number of seropositive ferrets occurred during the seventh wave when the different Omicron subvariants were the dominant virus variants. Our results suggest that the risk of SARS-CoV-2 transmission in domestic ferrets in natural conditions is low. Further research is need to evaluate the potential risk of transmission of SARS-CoV-2 from human to pets.

The online version contains supplementary material available at 10.1007/s11259-023-10190-2.

[end paper 43]

[begin paper 44]

PMCID = 8497067

Title = Simple workflow to repurpose SARS-CoV-2 swab/serum samples for the isolation of cost-effective antibody/antigens for proteotyping applications and diagnosis

Supply shortage for the development and production of preventive, therapeutic, and diagnosis tools during the COVID-19 pandemic is an important issue affecting the wealthy and poor nations alike. Antibodies and antigens are especially needed for the production of immunological-based testing tools such as point-of-care tests. Here, we propose a simple and quick magnetic nanoparticle (MNP)–based separation/isolation approach for the repurposing of infected human samples to produce specific antibodies and antigen cocktails. Initially, an antibody cocktail was purified from serums via precipitation and immunoaffinity chromatography. Purified antibodies were conjugated onto MNPs and used as an affinity matrix to separate antigens. The characterization process was performed by ELISA, SDS-PAGE, electrochemistry, isothermal titration calorimetry, and LC-Q-TOF-MS/MS analyses. The MNP-separated peptides can be used for mass spectrometry–based as well as paper-based lateral flow assay diagnostic. The exploitation of the current workflow for the development of efficient diagnostic tools, specific treatments, and fundamental research can significantly impact the present or eventual pandemic. This workflow can be considered as a two birds, one stone–like strategy.

The online version contains supplementary material available at 10.1007/s00216-021-03654-4.

[end paper 44]

[begin paper 45]

PMCID = 9937867

Title = Microbead-based extracorporeal immuno-affinity virus capture: a feasibility study to address the SARS-CoV-2 pandemic

In this paper, we report on the utilization of micro-technology based tools to fight viral infections. Inspired by various hemoperfusion and immune-affinity capture systems, a blood virus depletion device has been developed that offers highly efficient capture and removal of the targeted virus from the circulation, thus decreasing virus load. Single-domain antibodies against the Wuhan (VHH-72) virus strain produced by recombinant DNA technology were immobilized on the surface of glass micro-beads, which were then utilized as stationary phase. For feasibility testing, the virus suspension was flown through the prototype immune-affinity device that captured the viruses and the filtered media left the column. The feasibility test of the proposed technology was performed in a Biosafety Level 4 classified laboratory using the Wuhan SARS-CoV-2 strain. The laboratory scale device actually captured 120,000 virus particles from the culture media circulation proving the feasibility of the suggested technology. This performance has an estimated capture ability of 15 million virus particles by using the therapeutic size column design, representing three times over-engineering with the assumption of 5 million genomic virus copies in an average viremic patient. Our results suggested that this new therapeutic virus capture device could significantly lower virus load thus preventing the development of more severe COVID-19 cases and consequently reducing mortality rate.

The online version contains supplementary material available at 10.1007/s00604-023-05671-9.

[end paper 45]

[begin paper 46]

PMCID = 8569510

Title = In-solution buffer-free digestion allows full-sequence coverage and complete characterization of post-translational modifications of the receptor-binding domain of SARS-CoV-2 in a single ESI–MS spectrum

Subunit vaccines based on the receptor-binding domain (RBD) of the spike protein of SARS-CoV-2 provide one of the most promising strategies to fight the COVID-19 pandemic. The detailed characterization of the protein primary structure by mass spectrometry (MS) is mandatory, as described in ICHQ6B guidelines. In this work, several recombinant RBD proteins produced in five expression systems were characterized using a non-conventional protocol known as in-solution buffer-free digestion (BFD). In a single ESI–MS spectrum, BFD allowed very high sequence coverage (≥ 99%) and the detection of highly hydrophilic regions, including very short and hydrophilic peptides (2–8 amino acids), and the His6-tagged C-terminal peptide carrying several post-translational modifications at Cys538 such as cysteinylation, homocysteinylation, glutathionylation, truncated glutathionylation, and cyanylation, among others. The analysis using the conventional digestion protocol allowed lower sequence coverage (80–90%) and did not detect peptides carrying most of the above-mentioned PTMs. The two C-terminal peptides of a dimer [RBD(319–541)-(His)6]2 linked by an intermolecular disulfide bond (Cys538-Cys538) with twelve histidine residues were only detected by BFD. This protocol allows the detection of the four disulfide bonds present in the native RBD, low-abundance scrambling variants, free cysteine residues, O-glycoforms, and incomplete processing of the N-terminal end, if present. Artifacts generated by the in-solution BFD protocol were also characterized. BFD can be easily implemented; it has been applied to the characterization of the active pharmaceutical ingredient of two RBD-based vaccines, and we foresee that it can be also helpful to the characterization of mutated RBDs.

The online version contains supplementary material available at 10.1007/s00216-021-03721-w.

[end paper 46]

[begin paper 47]

PMCID = 8720170

Title = The Effects of ATIR Blocker on the Severity of COVID-19 in Hypertensive Inpatients and Virulence of SARS-CoV-2 in Hypertensive hACE2 Transgenic Mice

Angiotensin-converting enzyme 2 (ACE2) is required for the cellular entry of the severe acute respiratory syndrome coronavirus 2. ACE2, via the Ang-(1-7)-Mas-R axis, is part of the antihypertensive and cardioprotective effects of the renin-angiotensin system. We studied hospitalized COVID-19 patients with hypertension and hypertensive human(h) ACE2 transgenic mice to determine the outcome of COVID-19 with or without AT1 receptor (AT1R) blocker treatment. The severity of the illness and the levels of serum cardiac biomarkers (CK, CK-BM, cTnI), as well as the inflammation markers (IL-1, IL-6, CRP), were lesser in hypertensive COVID-19 patients treated with AT1R blockers than those treated with other antihypertensive drugs. Hypertensive hACE2 transgenic mice, pretreated with AT1R blocker, had increased ACE2 expression and SARS-CoV-2 in the kidney and heart, 1 day post-infection. We conclude that those hypertensive patients treated with AT1R blocker may be at higher risk for SARS-CoV-2 infection. However, AT1R blockers had no effect on the severity of the illness but instead may have protected COVID-19 patients from heart injury, via the ACE2-angiotensin1-7-Mas receptor axis.

The online version contains supplementary material available at 10.1007/s12265-021-10147-3.

[end paper 47]

[begin paper 48]

PMCID = 9940079

Title = Immunoinformatics Study of SARS-CoV-2 Nucleocapsid Phosphoprotein Identifies Promising Epitopes with Mutational Implications

The SARS-CoV-2 is rapidly evolving and new mutations are being reported from different parts of the world. In this study, we investigated the variations occurring in the nucleocapsid phosphoprotein (N-protein) of SARS-CoV-2 from India. We used several in silico prediction tools to characterise N-protein including IEDB webserver for B cell epitope prediction, Vaxijen 2.0 and AllergenFP v.1.0 for antigenicity and allergenicity prediction of epitopes, CLUSTAL Omega for mutation identification and PONDR webserver for disorder prediction, PROVEAN score for protein function and iMutantsuite for protein stability prediction. Our results show that 81 mutations have occurred in this protein among Indian SARS-CoV-2 isolates. Subsequently, we characterized the N-protein epitopes to identify seven most promising peptides. We mapped these mutations with seven N-protein epitopes to identify the loss of antigenicity in two of them, suggesting that the mutations occurring in the SARS-CoV-2 genome contribute to the alteration in the properties of epitopes. Altogether, our data strongly indicates that N-protein is gaining several mutations in its B cell epitope regions that might alter protein function.

[end paper 48]

[begin paper 49]

PMCID = 8412382

Title = Surface plasmon resonance aptasensor based on niobium carbide MXene quantum dots for nucleocapsid of SARS-CoV-2 detection

A novel label-free surface plasmon resonance (SPR) aptasensor has been constructed for the detection of N-gene of SARS-CoV-2 by using thiol-modified niobium carbide MXene quantum dots (Nb2C-SH QDs) as the bioplatform for anchoring N-gene-targeted aptamer. In the presence of SARS-CoV-2 N-gene, the immobilized aptamer strands changed their conformation to specifically bind with N-gene. It thus increased the contact area or enlarged the distance between aptamer and the SPR chip, resulting in a change of the SPR signal irradiated by the laser (He-Ne) with the wavelength (λ) of 633 nm. Nb2C QDs were derived from Nb2C MXene nanosheets via a solvothermal method, followed by functionalization with octadecanethiol through a self-assembling method. Subsequently, the gold chip for SPR measurements was modified with Nb2C-SH QDs via covalent binding of the Au-S bond also by self-assembling interaction. Nb2C-SH QDs not only resulted in high bioaffinity toward aptamer but also enhanced the SPR response. Thus, the Nb2C-SH QD-based SPR aptasensor had low limit of detection (LOD) of 4.9 pg mL−1 toward N-gene within the concentration range 0.05 to 100 ng mL−1. The sensor also showed excellent selectivity in the presence of various respiratory viruses and proteins in human serum and high stability. Moreover, the Nb2C-SH QD-based SPR aptasensor displayed a vast practical application for the qualitative analysis of N-gene from different samples, including seawater, seafood, and human serum. Thus, this work can provide a deep insight into the construction of the aptasensor for detecting SARS-CoV-2 in complex environments.

A novel label-free surface plasmon resonance aptasensor has been constructed to detect sensitively and selectively the N-gene of SARS-CoV-2 by using thiol-modified niobium carbide MXene quantum dots as the scaffold to anchor the N-gene-targeted aptamer.

The online version contains supplementary material available at 10.1007/s00604-021-04974-z.

[end paper 49]

[begin paper 50]

PMCID = 11211828

Title = DDAffinity: predicting the changes in binding affinity of multiple point mutations using protein 3D structure

Mutations are the crucial driving force for biological evolution as they can disrupt protein stability and protein–protein interactions which have notable impacts on protein structure, function, and expression. However, existing computational methods for protein mutation effects prediction are generally limited to single point mutations with global dependencies, and do not systematically take into account the local and global synergistic epistasis inherent in multiple point mutations.

To this end, we propose a novel spatial and sequential message passing neural network, named DDAffinity, to predict the changes in binding affinity caused by multiple point mutations based on protein 3D structures. Specifically, instead of being on the whole protein, we perform message passing on the k-nearest neighbor residue graphs to extract pocket features of the protein 3D structures. Furthermore, to learn global topological features, a two-step additive Gaussian noising strategy during training is applied to blur out local details of protein geometry. We evaluate DDAffinity on benchmark datasets and external validation datasets. Overall, the predictive performance of DDAffinity is significantly improved compared with state-of-the-art baselines on multiple point mutations, including end-to-end and pre-training based methods. The ablation studies indicate the reasonable design of all components of DDAffinity. In addition, applications in nonredundant blind testing, predicting mutation effects of SARS-CoV-2 RBD variants, and optimizing human antibody against SARS-CoV-2 illustrate the effectiveness of DDAffinity.

DDAffinity is available at https://github.com/ak422/DDAffinity.

[end paper 50]

[begin paper 51]

PMCID = 8036011

Title = Accuracy of the serological detection of IgG and IgM to SARS-Cov-2: a prospective, cross-sectional study

In response to the rapidly evolving of SARS-CoV-2 infection, numerous serological tests have been developed but their sensitivity and specificity are unclear. We collected serum samples of patients and health-care professionals to assess the accuracy of chemiluminescent (CLIA) and two lateral flow immunochromatographic assays (LFIA) to determine IgG and IgM antibodies to SARS-CoV-2 virus. We calculated the φ correlation for qualitative results and test accuracy, adopting the following case definition: either real-time-PCR positivity or serological positivity with at least two different tests. We analyzed 259 samples, obtaining strong correlation between CLIA and both LFIA for IgG (φ=0.9), and moderate correlation for IgM (φ=0.6). For patients, the sensitivity was suboptimal for all methods (CLIA 81%, LFIA A 85%, LFIA B 78%), while it was poor in asymptomatic health-care workers (CLIA 50%, LFIA A 50%, LFIA B 33%). Overall, CLIA is more sensitive and specific for the determination of both IgG and IgM, whilst both LFIA methods reported good sensitivity and specificity for IgG, but scarce sensitivity for the IgM determination. The determination of SARS-CoV-2-specific IgG is useful to detect infection 6 days from symptom onset.

The online version contains supplementary material available at 10.1007/s10096-021-04224-3.

[end paper 51]

[begin paper 52]

PMCID = 8166382

Title = Simultaneous detection of the spike and nucleocapsid proteins from SARS-CoV-2 based on ultrasensitive single molecule assays

Nucleic acid detection technology based on polymerase chain reaction (PCR) and antibody detection based on immunochromatography still have many problems such as false negatives for the diagnosis of coronavirus disease 2019 (COVID-19). Therefore, it is of great importance to develop new techniques to improve the diagnostic accuracy of COVID-19. We herein developed an ultrasensitive, rapid, and duplex digital enzyme-linked immunosorbent assay (dELISA) for simultaneous detection of spike (S-RBD) and nucleocapsid (N) proteins of SARS-CoV-2 based on a single molecule array. This assay effectively combines magnetic bead encoding technology and the ultrasensitive detection capability of a single molecule array. The detection strategies of S-RBD protein and N-protein exhibited wide response ranges of 0.34–1065 pg/mL and 0.183–338 pg/mL with detection limits of 20.6 fg/mL and 69.8 fg/mL, respectively. It is a highly specific method for the simultaneous detection of S-RBD protein and N-protein and has minimal interference from other blood proteins. Moreover, the spike assay showed a satisfactory and reproducible recovery rate for the detection of S-RBD protein and N-protein in serum samples. Overall, this work provides a highly sensitive method for the simultaneous detection of S-RBD protein and N-protein, which shows ultrasensitivity and high signal-to-noise ratio and contributes to improve the diagnosis accuracy of COVID-19.

The online version contains supplementary material available at 10.1007/s00216-021-03435-z.

[end paper 52]

[begin paper 53]

PMCID = 8428493

Title = Development and application of a SARS-CoV-2 colorimetric biosensor based on the peroxidase-mimic activity of γ-Fe2O3 nanoparticles

A practical colorimetric assay was developed for the detection of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). For this purpose, magnetic γ Fe2O3 nanoparticles were synthesized and used as a peroxidase-like mimic activity molecule. In the presence of γ Fe2O3 nanoparticles, the color change of H2O2 included 3,3′,5,5′-tetramethylbenzidine was monitored at the wavelength of 654 nm when spike protein interacted with angiotensin-converting enzyme 2 receptor. This oxidation-reduction reaction was examined both spectroscopically and by using electrochemical techniques. The experimental parameters were optimized and the analytical characteristics investigated. The developed assay was applied to real SARS-CoV-2 samples, and very good results that were in accordance with the real time polymerase chain reaction were obtained.

The online version contains supplementary material available at 10.1007/s00604-021-04989-6.

[end paper 53]

[begin paper 54]

PMCID = 11204317

Title = Exploring the Pathophysiology of Long COVID: The Central Role of Low-Grade Inflammation and Multisystem Involvement

Long COVID (LC), also referred to as Post COVID-19 Condition, Post-Acute Sequelae of SARS-CoV-2 Infection (PASC), and other terms, represents a complex multisystem disease persisting after the acute phase of COVID-19. Characterized by a myriad of symptoms across different organ systems, LC presents significant diagnostic and management challenges. Central to the disorder is the role of low-grade inflammation, a non-classical inflammatory response that contributes to the chronicity and diversity of symptoms observed. This review explores the pathophysiological underpinnings of LC, emphasizing the importance of low-grade inflammation as a core component. By delineating the pathogenetic relationships and clinical manifestations of LC, this article highlights the necessity for an integrated approach that employs both personalized medicine and standardized protocols aimed at mitigating long-term consequences. The insights gained not only enhance our understanding of LC but also inform the development of therapeutic strategies that could be applicable to other chronic conditions with similar pathophysiological features.

[end paper 54]

[begin paper 55]

PMCID = 9261893

Title = Allosteric Modulation of the Main Protease (MPro) of SARS-CoV-2 by Casticin—Insights from Molecular Dynamics Simulations

Inhibition of the main protease (Mpro) of SARS-CoV-2 has been suggested to be vital in shutting down viral replication in a host. Most efforts aimed at inhibiting MPro activity have been channeled into competitive inhibition at the active site, but this strategy will require a high inhibitor concentration and impressive inhibitor-MPro binding affinity. Allosteric inhibition can potentially serve as an effective strategy for alleviating these limitations. In this study, the ability of antiviral natural products to inhibit MPro in an allosteric fashion was explored with in silico techniques. Molecular docking revealed a strong interaction between casticin, an antiviral flavonoid, and Mpro at a site distant from the active site. This site, characterized as a distal site, has been shown to have an interdependent dynamic effect with the active site region. Mpro only, Mpro-peptide (binary) and Mpro-peptide-casticin (ternary) complexes were subjected to molecular dynamics simulations for 50 ns to investigate the modulatory activity of casticin binding on Mpro. Molecular dynamic simulations revealed that binding of casticin at the distal site interferes with the proper orientation of the peptide substrate in the oxyanion hole of the active site, and this could lead to a halt or decrease in catalytic activity. This study therefore highlights casticin as a potential allosteric modulator of the SARS-CoV-2 main protease, which could be optimized and developed into a potential lead compound for anti-SARS-CoV-2 chemotherapy.

The online version contains supplementary material available at 10.1007/s42250-022-00411-7.

[end paper 55]

[begin paper 56]

PMCID = 8359636

Title = Deciphering epigenetic(s) role in modulating susceptibility to and severity of COVID-19 infection and/or outcome: a systematic rapid review

COVID-19 pandemic waves hitting worldwide result in drastic postinfection complications with interindividual variations, which raised the question for the cause of these observed variations. This urged to think “the impact of environment-affected genes”? In an attempt to unravel the impact of environment-affected genes, a systematic rapid review was conducted to study “the impact of host or viral epigenetic modulation on COVID-19 infection susceptibility and/or outcome.” Electronic databases including Web of Science, SCOPUS, Cochrane Central Register of Controlled Trials, PubMed, and Google Scholar, and other databases were searched. The search strings included “COVID-19” OR “SARS-CoV-2” AND (Epigenetics’). Articles with randomized clinical trials (RCTs) and observational study designs, conducted on humans and available in the English language, were selected, with respect to “The interplay between the SARS-CoV-2 virus and Epigenetics” published from 2020 to February 2021 (but not limited to 2020, being expanded to 2015). Database search yielded 1330 articles; after screening, exclusion, and further filtrations, 51 articles were included. Susceptibility to COVID-19 infection is related to the viral-microRNAs (miRNAs) which alter virulence of the transmitted SARS-CoV-2 strains and impact host-miRNA-related innate immunity. Host-DNA methylation and/or chromatin remodeling may be implicated in severe cytokine storm that can ultimately results in fatal outcome.

The online version contains supplementary material available at 10.1007/s11356-021-15588-6.

[end paper 56]

[begin paper 57]

PMCID = 11725859

Title = Learning the language of antibody hypervariability

Antibodies are crucial in therapeutics and immune defense, but their hypervariable regions pose challenges for computational modeling. We introduce Antibody Mutagenesis-Augmented Processing (AbMAP), a transfer learning framework that adapts foundational protein language models to antibody-specific tasks. AbMAP focuses on the hypervariable regions, employing contrastive augmentation and multitask learning to capture both structural and functional properties. This approach significantly improves prediction accuracy for various antibody properties, including antigen binding and paratope identification. AbMAP demonstrates high efficiency in antibody optimization, achieving an 82% hit rate in refining SARS-CoV-2-binding antibodies. Importantly, it unlocks large-scale analysis of immune repertoires, revealing surprising structural and functional convergence across individuals despite sequence diversity.

Protein language models (PLMs) have demonstrated impressive success in modeling proteins. However, general-purpose “foundational” PLMs have limited performance in modeling antibodies due to the latter’s hypervariable regions, which do not conform to the evolutionary conservation principles that such models rely on. In this study, we propose a transfer learning framework called Antibody Mutagenesis-Augmented Processing (AbMAP), which fine-tunes foundational models for antibody-sequence inputs by supervising on antibody structure and binding specificity examples. Our learned feature representations accurately predict mutational effects on antigen binding, paratope identification, and other key antibody properties. We experimentally validate AbMAP for antibody optimization by applying it to refine a set of antibodies that bind to a SARS-CoV-2 peptide, and obtain an 82% hit-rate and up to 22-fold increase in binding affinity. AbMAP also unlocks large-scale analyses of immune repertoires, revealing that B-cell receptor repertoires of individuals, while remarkably different in sequence, converge toward similar structural and functional coverage. Importantly, AbMAP’s transfer learning approach can be readily adapted to advances in foundational PLMs. We anticipate AbMAP will accelerate the efficient design and modeling of antibodies, expedite the discovery of antibody-based therapeutics, and deepen our understanding of humoral immunity.

[end paper 57]

[begin paper 58]

PMCID = 9244507

Title = Recent advances in antiviral effects of probiotics: potential mechanism study in prevention and treatment of SARS-CoV-2

SARS-CoV-2 is responsible for coronavirus disease 2019 (COVID-19), progressively extended worldwide countries on an epidemic scale. Along with all the drug treatments suggested to date, currently, there are no approved management protocols and treatment regimens for SARS-CoV-2. The unavailability of optimal medication and effective vaccines against SARS-CoV-2 indicates the requirement for alternative therapies. Probiotics are living organisms that deliberate beneficial effects on the host when used sufficiently and in adequate amounts, and fermented food is their rich source. Probiotics affect viruses by antiviral mechanisms and reduce diarrhea and respiratory tract infection. At this point, we comprehensively evaluated the antiviral effects of probiotics and their mechanism with a particular focus on SARS-CoV-2. In this review, we suggested the conceptual and potential mechanisms of probiotics by which they could exhibit antiviral properties against SARS-CoV-2, according to the previous evidence concerning the mechanism of antiviral effects of probiotics. This study reviewed recent studies that speculate about the role of probiotics in the prevention of the SARS-CoV-2-induced cytokine storm through the mechanisms such as induction of anti-inflammatory cytokines (IL-10), downregulation of pro-inflammatory cytokines (TNF-α, IL-2, IL-6), inhibition of JAK signaling pathway, and act as HDAC inhibitor. Also, the recent clinical trials and their outcome have been reviewed.

The online version contains supplementary material available at 10.1007/s11756-022-01147-y.

[end paper 58]

[begin paper 59]

PMCID = 10869273

Title = Efficient evolution of human antibodies from general protein language models

Natural evolution must explore a vast landscape of possible sequences for desirable yet rare mutations, suggesting that learning from natural evolutionary strategies could guide artificial evolution. Here we report that general protein language models can efficiently evolve human antibodies by suggesting mutations that are evolutionarily plausible, despite providing the model with no information about the target antigen, binding specificity or protein structure. We performed language-model-guided affinity maturation of seven antibodies, screening 20 or fewer variants of each antibody across only two rounds of laboratory evolution, and improved the binding affinities of four clinically relevant, highly mature antibodies up to sevenfold and three unmatured antibodies up to 160-fold, with many designs also demonstrating favorable thermostability and viral neutralization activity against Ebola and severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) pseudoviruses. The same models that improve antibody binding also guide efficient evolution across diverse protein families and selection pressures, including antibiotic resistance and enzyme activity, suggesting that these results generalize to many settings.

A general protein language model guides protein evolution with 20 or fewer variants needed for testing.

[end paper 59]

[begin paper 60]

PMCID = 10418099

Title = Biophysical principles predict fitness of SARS-CoV-2 variants

SARS-CoV-2 employs its spike protein’s receptor binding domain (RBD) to enter host cells. The RBD is constantly subjected to immune responses, while requiring efficient binding to host cell receptors for successful infection. However, our understanding of how RBD’s biophysical properties contribute to SARS-CoV-2’s epidemiological fitness remains largely incomplete. Through a comprehensive approach, comprising large-scale sequence analysis of SARS-CoV-2 variants and the discovery of a fitness function based on binding thermodynamics, we unravel the relationship between the biophysical properties of RBD variants and their contribution to viral fitness. We developed a biophysical model that uses statistical mechanics to map the molecular phenotype space, characterized by binding constants of RBD to ACE2, LY-CoV016, LY-CoV555, REGN10987, and S309, onto a epistatic fitness landscape. We validate our findings through experimentally measured and machine learning (ML) estimated binding affinities, coupled with infectivity data derived from population-level sequencing. Our analysis reveals that this model effectively predicts the fitness of novel RBD variants and can account for the epistatic interactions among mutations, including explaining the later reversal of Q493R. Our study sheds light on the impact of specific mutations on viral fitness and delivers a tool for predicting the future epidemiological trajectory of previously unseen or emerging low frequency variants. These insights offer not only greater understanding of viral evolution but also potentially aid in guiding public health decisions in the battle against COVID-19 and future pandemics.

[end paper 60]

[begin paper 61]

PMCID = 10886287

Title = Leveraging Artificial Intelligence to Expedite Antibody Design and Enhance Antibody–Antigen Interactions

This perspective sheds light on the transformative impact of recent computational advancements in the field of protein therapeutics, with a particular focus on the design and development of antibodies. Cutting-edge computational methods have revolutionized our understanding of protein–protein interactions (PPIs), enhancing the efficacy of protein therapeutics in preclinical and clinical settings. Central to these advancements is the application of machine learning and deep learning, which offers unprecedented insights into the intricate mechanisms of PPIs and facilitates precise control over protein functions. Despite these advancements, the complex structural nuances of antibodies pose ongoing challenges in their design and optimization. Our review provides a comprehensive exploration of the latest deep learning approaches, including language models and diffusion techniques, and their role in surmounting these challenges. We also present a critical analysis of these methods, offering insights to drive further progress in this rapidly evolving field. The paper includes practical recommendations for the application of these computational techniques, supplemented with independent benchmark studies. These studies focus on key performance metrics such as accuracy and the ease of program execution, providing a valuable resource for researchers engaged in antibody design and development. Through this detailed perspective, we aim to contribute to the advancement of antibody design, equipping researchers with the tools and knowledge to navigate the complexities of this field.

[end paper 61]

[begin paper 62]

PMCID = 7787249

Title = Brain Disease Network Analysis to Elucidate the Neurological Manifestations of COVID-19

Although COVID-19 largely causes respiratory complications, it can also lead to various extrapulmonary manifestations resulting in higher mortality and these comorbidities are posing a challenge to the health care system. Reports indicate that 30–60% of patients with COVID-19 suffer from neurological symptoms. To understand the molecular basis of the neurologic comorbidity in COVID-19 patients, we have investigated the genetic association between COVID-19 and various brain disorders through a systems biology-based network approach and observed a remarkable resemblance. Our results showed 123 brain-related disorders associated with COVID-19 and form a high-density disease-disease network. The brain-disease-gene network revealed five highly clustered modules demonstrating a greater complexity of COVID-19 infection. Moreover, we have identified 35 hub proteins of the network which were largely involved in the protein catabolic process, cell cycle, RNA metabolic process, and nuclear transport. Perturbing these hub proteins by drug repurposing will improve the clinical conditions in comorbidity. In the near future, we assumed that in COVID-19 patients, many other neurological manifestations will likely surface. Thus, understanding the infection mechanisms of SARS-CoV-2 and associated comorbidity is a high priority to contain its short- and long-term effects on human health. Our network-based analysis strengthens the understanding of the molecular basis of the neurological manifestations observed in COVID-19 and also suggests drug for repurposing.

The online version contains supplementary material available at 10.1007/s12035-020-02266-w.

[end paper 62]

[begin paper 63]

PMCID = 8744046

Title = Naturally occurring anthraquinones as potential inhibitors of SARS-CoV-2 main protease: an integrated computational study

The novel coronavirus disease (COVID-19) has spread throughout the globe, affecting millions of people. The World Health Organization (WHO) has declared this infectious disease a pandemic. At present, several clinical trials are going on to identify possible drugs for treating this infection. SARS-CoV-2 Mpro is one of the most critical drug targets for the blockage of viral replication. The aim of this study was to identify potential natural anthraquinones that could bind to the active site of SARS-CoV-2 main protease and stop the viral replication. Blind molecular docking studies of 13 anthraquinones and one control drug (Boceprevir) with SARS-CoV-2 Mpro were carried out using the SwissDOCK server, and alterporriol-Q that showed the highest binding affinity towards Mpro were subjected to molecular dynamics simulation studies. This study indicated that several antiviral anthraquinones could prove to be effective inhibitors for SARS-CoV-2 Mpro of COVID-19 as they bind near the active site having the catalytic dyad, HIS41 and CYS145 through non-covalent forces. The anthraquinones showed less inhibitory potential as compared to the FDA-approved drug, boceprevir. Among the anthraquinones studied, alterporriol-Q was found to be the most potent inhibitor of SARS-CoV-2 Mpro. Further, MD simulation studies for Mpro- alterporriol-Q system suggested that alterporriol-Q does not alter the structure of Mpro to a significant extent. Considering the impact of COVID-19, identification of alternate compounds like alterporriol-Q that could inhibit the viral infection will help in accelerating the process of drug discovery.

The online version contains supplementary material available at 10.1007/s11756-021-01004-4.

[end paper 63]

[begin paper 64]

PMCID = 9760608

Title = Impact of BNT162b2 mRNA anti-SARS-CoV-2 vaccine on interferon-alpha production by plasmacytoid dendritic cells and autoreactive T cells in patients with systemic lupus erythematosus: The COVALUS project

To evaluate the specific response of SLE patients to BNT162b2 vaccination and its impact on autoimmunity defined as in vivo production of interferon-alpha (IFNα) by plasmacytoid dendritic cells (pDCs) and autoreactive immune responses.

Our prospective study included SLE patients and healthy volunteers (HV) who received 2 doses of BNT162b2 vaccine 4 weeks apart. Subjects under immunosuppressive drugs or with evidence of prior COVID-19 were excluded. IgG anti-Spike SARS-CoV-2 (anti-S) antibodies, anti-S specific-B cells, anti-S specific T cells, in vivo INF-α production by pDCs, activation marker expression by pDCs and autoreactive anti-nuclear T cells were quantified before first injection, before second injection, and 3 and 6 months after first injection.

Vaccinated SLE patients produced significantly lower IgG antibodies and specific B cells against SARS–CoV-2 as compared to HV. In contrast, anti-S T cell response did not significantly differ between SLE patients and HV. Following vaccination, the surface expression of HLA-DR and CD86 and the in vivo production of IFNα by pDCs significantly increased in SLE patients. The boosted expression of HLA-DR on pDCs induced by BNT162b2 vaccine correlated with the overall immune responses against SARS-CoV-2 (anti-S antibodies: r = 0.27 [0.05–0.46], p = 0.02; anti-S B cells: r = 0.19 [-0.03-0.39], p = 0.09); anti-S T cells: r = 0.28 [0.05–0.47], p = 0.016). Eventually, anti-SARS-CoV-2 vaccination was associated with an overall decrease of autoreactive T cells (slope = - 0.00067, p = 0.015).

BNT162b2 vaccine induces a transient in vivo activation of pDCs in SLE that contributes to the immune responses against SARS-CoV-2. Unexpectedly BNT162b2 vaccine also dampens the pool of circulating autoreactive T cells, suggesting that vaccination may have a beneficial impact on SLE disease.

[end paper 64]

[begin paper 65]

PMCID = 8982303

Title = Seroprevalence of SARS-CoV-2 antibodies among blood donors in Québec: an update from a serial cross-sectional study

We previously estimated the seroprevalence of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) antibodies following the first pandemic wave at 2.23% in Québec, Canada. Following the much bigger second wave in fall 2020 and early 2021, we estimated the seroprevalence of anti-SARS-CoV-2 in Québec during the first months of 2021.

Blood samples from regular, asymptomatic (for ≥ 14 days) donors were collected between January 25, 2021 and March 11, 2021. Anti-SARS-CoV-2 seropositivity was assessed using an enzyme-linked immunosorbent assay that captures antibodies directed against the receptor binding domain of the SARS-CoV-2 spike (and hence cannot discriminate between infection- and vaccine-induced seropositivity). Seroprevalence estimates were adjusted for regional distribution, age, and sex.

Samples from 7924 eligible donors were analyzed, including 620 (7.8%) vaccinated donors and 7046 (88.9%) unvaccinated donors (vaccination status unknown for 258 (3.3%) donors). Overall, median age was 51 years; 46.4% of donors were female. The adjusted seroprevalence was 10.5% (95% CI = 9.7–11.3) in the unvaccinated population and 14.7% (95% CI = 13.8–15.6) in the overall population. Seroprevalence gradually decreased with age and was higher among donors who self-identified as having a racial/ethnic background other than white, both in the overall and in the unvaccinated populations.

The seroprevalence of SARS-CoV-2 antibodies significantly increased in Québec since spring 2020, with younger persons and ethnic minorities being disproportionately affected. When compared with the cumulative incidence rate reported by public health authorities (i.e., 3.3% as of March 11, 2021), these results suggest that a substantial proportion of infections remain undetected despite improvements in access to COVID-19 testing.

The online version contains supplementary material available at 10.17269/s41997-022-00622-y.

[end paper 65]

[begin paper 66]

PMCID = 7541098

Title = Antibody response to multiple antigens of SARS-CoV-2 in patients with diabetes: an observational cohort study

The aim of the study was to characterise the humoral response against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in patients with diabetes. Demonstrating the ability to mount an appropriate antibody response in the presence of hyperglycaemia is relevant for the comprehension of mechanisms related to the observed worse clinical outcome of coronavirus disease 2019 (COVID-19) pneumonia in patients with diabetes and for the development of any future vaccination campaign to prevent SARS-CoV-2 infection.

Using a highly specific and sensitive measurement of antibodies by fluid-phase luciferase immunoprecipitation assays, we characterised the IgG, IgM and IgA response against multiple antigens of SARS-CoV-2 in a cohort of 509 patients with documented diagnosis of COVID-19, prospectively followed at our institution. We analysed clinical outcomes and antibody titres according to the presence of hyperglycaemia, i.e., either diagnosed or undiagnosed diabetes, at the time of, or during, hospitalisation.

Among patients with confirmed COVID-19, 139 (27.3%) had diabetes: 90 (17.7%) had diabetes diagnosed prior to the hospital admission (comorbid diabetes) while 49 (9.6%) had diabetes diagnosed at the time of admission (newly diagnosed). Diabetes was associated with increased levels of inflammatory biomarkers and hypercoagulopathy, as well as leucocytosis and neutrophilia. Diabetes was independently associated with risk of death (HR 2.32 [95% CI 1.44, 3.75], p = 0.001), even after adjustment for age, sex and other relevant comorbidities. Moreover, a strong association between higher glucose levels and risk of death was documented irrespective of diabetes diagnosis (HR 1.14 × 1.1 mmol/l [95% CI 1.08, 1.21], p < 0.001). The humoral response against SARS-CoV-2 in patients with diabetes was present and superimposable, as for timing and antibody titres, to that of non-diabetic patients, with marginal differences, and was not influenced by glucose levels. Of the measured antibody responses, positivity for IgG against the SARS-CoV-2 spike receptor-binding domain (RBD) was predictive of survival rate, both in the presence or absence of diabetes.

The observed increased severity and mortality risk of COVID-19 pneumonia in patients with hyperglycaemia was not the result of an impaired humoral response against SARS-CoV-2. RBD IgG positivity was associated with a remarkable protective effect, allowing for a cautious optimism about the efficacy of future vaccines against SARs-COV-2 in people with diabetes.

Graphical abstract

The online version of this article (10.1007/s00125-020-05284-4) contains peer-reviewed but unedited supplementary material, which is available to authorised users.

[end paper 66]

[begin paper 67]

PMCID = 8800849

Title = Inhibitory efficacy of 2, 4-diacetylphloroglucinol against SARS-COV-2 proteins: in silico study

The pandemic of Severe Acute Respiratory Syndrome Coronavirus-2 has affected millions of people worldwide with common symptoms of fever, cough, and respiratory complications. The pandemic has posed a huge challenge to emergency health services due to unavailability of potent therapeutic drugs. The proteins associated with the viral pathogenesis has been identified as suitable targets for drug design and warrants effective drug discovery to abate COVID-19. The papain-like protease (PLpro), nucleocapsid (N), main protease (Mpro) and non-structural protein (nsp12) of SARS-CoV-2, key component of processing of viral polyproteins, transcription, assembly and replication. On this streak, present study evaluated the interaction of ligand 2,4-diacetylphloroglucinol (DAPG) with viral proteins using molecular docking with (i) AutoDock 4.2.6 and (ii) AutoDock Vina followed by molecular dynamic simulation studies of protein-ligand complex configuration. The analysis revealed that PLpro (3E9S) and N (4J3K) protein corresponds to the highest docking score and therefore, selected for molecular dynamics simulation study (100 ns). The study comprised analysis of parameters: (i) RMSD and RMSF, (ii) radius of gyration- which indicated interaction of protein entities with ligand supported steadiness of the complex, (iii) Coulombic and Lennard–Jones interactions, which played a significant role in complex stability. DAPG showed a good number of H-bonds with PLpro and MM-PBSA binding energy when compared to the N protein. This study showed DAPG as a potential bioactive molecule to act as an inhibitor for the PLpro thereby, DAPG can be used as potential inhibitor against SARS-CoV-2 and is potential drug candidate against COVID-19.

The online version contains supplementary material available at 10.1007/s11756-021-00979-4.

[end paper 67]

[begin paper 68]

PMCID = 8175097

Title = Performance of a SARS CoV-2 antibody ELISA based on simultaneous measurement of antibodies against the viral nucleoprotein and receptor-binding domain

SARS CoV-2 antibody assays measure antibodies against the viral nucleoprotein (NP) or spike protein. The study examined if testing of antibodies against both antigens increases the diagnostic sensitivity. Sera (N=98) from infected individuals were tested with ELISAs based on the NP, receptor-binding domain (RBD), or both proteins. The AUROCs were 0.958 (NP), 0.991 (RBD), and 0.992 (NP/RBD). The RBD- and NP/RBD-based ELISAs showed better performance than the NP-based assay. Simultaneous testing for antibodies against NP and RBD increased the number of true and false positives. If maximum diagnostic sensitivity is required, the NP/RBD-based ELISA is preferable. Otherwise, the RBD-based ELISA is sufficient.

The online version contains supplementary material available at 10.1007/s10096-021-04284-5.

[end paper 68]

[begin paper 69]

PMCID = 7998085

Title = Essentials in saline pharmacology for nasal or respiratory hygiene in times of COVID-19

Nasal irrigation or nebulizing aerosol of isotonic or hypertonic saline is a traditional method for respiratory or nasal care. A recent small study in outpatients with COVID-19 without acute respiratory distress syndrome suggests substantial symptom resolution. We therefore analyzed pharmacological/pharmacodynamic effects of isotonic or hypertonic saline, relevant to SARS-CoV-2 infection and respiratory care.

Mixed search method.

Due to its wetting properties, saline achieves an improved spreading of alveolar lining fluid and has been shown to reduce bio-aerosols and viral load. Saline provides moisture to respiratory epithelia and gels mucus, promotes ciliary beating, and improves mucociliary clearance. Coronaviruses and SARS-CoV-2 damage ciliated epithelium in the nose and airways. Saline inhibits SARS-CoV-2 replication in Vero cells; possible interactions involve the viral ACE2-entry mechanism (chloride-dependent ACE2 configuration), furin and 3CLpro (inhibition by NaCl), and the sodium channel ENaC. Saline shifts myeloperoxidase activity in epithelial or phagocytic cells to produce hypochlorous acid. Clinically, nasal or respiratory airway care with saline reduces symptoms of seasonal coronaviruses and other common cold viruses. Its use as aerosol reduces hospitalization rates for bronchiolitis in children. Preliminary data suggest symptom reduction in symptomatic COVID-19 patients if saline is initiated within 48 h of symptom onset.

Saline interacts at various levels relevant to nasal or respiratory hygiene (nasal irrigation, gargling or aerosol). If used from the onset of common cold symptoms, it may represent a useful add-on to first-line interventions for COVID-19. Formal evaluation in mild COVID-19 is desirable as to establish efficacy and optimal treatment regimens.

The online version contains supplementary material available at 10.1007/s00228-021-03102-3.

[end paper 69]

[begin paper 70]

PMCID = 8716573

Title = Embeddings from protein language models predict conservation and variant effects

The emergence of SARS-CoV-2 variants stressed the demand for tools allowing to interpret the effect of single amino acid variants (SAVs) on protein function. While Deep Mutational Scanning (DMS) sets continue to expand our understanding of the mutational landscape of single proteins, the results continue to challenge analyses. Protein Language Models (pLMs) use the latest deep learning (DL) algorithms to leverage growing databases of protein sequences. These methods learn to predict missing or masked amino acids from the context of entire sequence regions. Here, we used pLM representations (embeddings) to predict sequence conservation and SAV effects without multiple sequence alignments (MSAs). Embeddings alone predicted residue conservation almost as accurately from single sequences as ConSeq using MSAs (two-state Matthews Correlation Coefficient—MCC—for ProtT5 embeddings of 0.596 ± 0.006 vs. 0.608 ± 0.006 for ConSeq). Inputting the conservation prediction along with BLOSUM62 substitution scores and pLM mask reconstruction probabilities into a simplistic logistic regression (LR) ensemble for Variant Effect Score Prediction without Alignments (VESPA) predicted SAV effect magnitude without any optimization on DMS data. Comparing predictions for a standard set of 39 DMS experiments to other methods (incl. ESM-1v, DeepSequence, and GEMME) revealed our approach as competitive with the state-of-the-art (SOTA) methods using MSA input. No method outperformed all others, neither consistently nor statistically significantly, independently of the performance measure applied (Spearman and Pearson correlation). Finally, we investigated binary effect predictions on DMS experiments for four human proteins. Overall, embedding-based methods have become competitive with methods relying on MSAs for SAV effect prediction at a fraction of the costs in computing/energy. Our method predicted SAV effects for the entire human proteome (~ 20 k proteins) within 40 min on one Nvidia Quadro RTX 8000. All methods and data sets are freely available for local and online execution through bioembeddings.com, https://github.com/Rostlab/VESPA, and PredictProtein.

The online version contains supplementary material available at 10.1007/s00439-021-02411-y.

[end paper 70]

[begin paper 71]

PMCID = 10942297

Title = Novel antibody language model accelerates IgG screening and design for broad-spectrum antiviral therapy

Therapeutic antibodies have become one of the most influential therapeutics in modern medicine to fight against infectious pathogens, cancer, and many other diseases. However, experimental screening for highly efficacious targeting antibodies is labor-intensive and of high cost, which is exacerbated by evolving antigen targets under selective pressure such as fast-mutating viral variants. As a proof-of-concept, we developed a machine learning-assisted antibody generation pipeline AbGen that greatly accelerates the screening and re-design of immunoglobulins G (IgGs) against a broad spectrum of SARS-CoV-2 coronavirus variant strains. Our AbGen centers around a novel antibody language model (AbLM) that is pretrained on 12 million generic protein domain sequences and fine-tuned on 4,000+ paired VH-VL sequences, with IgG-specific CDR-masking and VH-VL cross-attention. AbLM provides a latent space of IgG sequence embeddings for AbGen, including (a) landscapes of IgGs’ activities in neutralizing the wild-type virus are analyzed through structure prediction for IgG and IgG-antigen (viral protein spike’s receptor binding domain, RBD) interactions; and (b) landscapes of IgGs’ susceptibility in neutralizing variant viruses are predicted through Gaussian process regression, despite that as few as 14 clinical antibodies’ responses to variants of concern are available. The AbGen pipeline was applied to over 1300 IgG sequences we collected from RBD-binding B cells of convalescent patients. With experimental validations, AbGen efficiently prioritized IgG candidates against a broad spectrum of viral variants (wildtype, Delta, and Omicron), preventing the infection of host cells in vitro and hACE2 transgenic mice in vivo. Compared to other existing protein language models that require 10–100 times more model parameters, AbLM improved the precision from around 50% to 75% to predict IgGs with low variant susceptibility. Furthermore, AbGen enables structure-based computational protein redesign for selected IgG clones with single amino acid substitutions at the RBD-binding interface that doubled the IgG blockade efficacy for one of the severe, therapy-resistant strains - Delta (B.1.617). Our work expedites applications of artificial intelligence in antibody screen and re-design combining data-driven protein language models and Kriging for antibody sequence analysis and activity prediction, in synergy with physics-driven protein docking and design for antibody-antigen interface analyses and functional optimization.

[end paper 71]

[begin paper 72]

PMCID = 9038526

Title = Mild COVID-19 imprints a long-term inflammatory eicosanoid- and chemokine memory in monocyte-derived macrophages

Monocyte-derived macrophages (MDM) drive the inflammatory response to severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) and they are a major source of eicosanoids in airway inflammation. Here we report that MDM from SARS-CoV-2-infected individuals with mild disease show an inflammatory transcriptional and metabolic imprint that lasts for at least 5 months after SARS-CoV-2 infection. MDM from convalescent SARS-CoV-2-infected individuals showed a downregulation of pro-resolving factors and an increased production of pro-inflammatory eicosanoids, particularly 5-lipoxygenase-derived leukotrienes. Leukotriene synthesis was further enhanced by glucocorticoids and remained elevated at 3–5 months, but had returned to baseline at 12 months post SARS-CoV-2 infection. Stimulation with SARS-CoV-2 spike protein or LPS triggered exaggerated prostanoid-, type I IFN-, and chemokine responses in post COVID-19 MDM. Thus, SARS-CoV-2 infection leaves an inflammatory imprint in the monocyte/ macrophage compartment that drives aberrant macrophage effector functions and eicosanoid metabolism, resulting in long-term immune aberrations in patients recovering from mild COVID-19.

[end paper 72]

[begin paper 73]

PMCID = 11794456

Title = DeepPFP: a multi-task-aware architecture for protein function prediction

Deriving protein function from protein sequences poses a significant challenge due to the intricate relationship between sequence and function. Deep learning has made remarkable strides in predicting sequence-function relationships. However, models tailored for specific tasks or protein types encounter difficulties when using transfer learning across domains. This is attributed to the fact that protein function relies heavily on structural characteristics rather than mere sequence information. Consequently, there is a pressing need for a model capable of capturing shared features among diverse sequence-function mapping tasks to address the generalization issue. In this study, we explore the potential of Model-Agnostic Meta-Learning combined with a protein language model called Evolutionary Scale Modeling to tackle this challenge. Our approach involves training the architecture on five out-domain deep mutational scanning (DMS) datasets and evaluating its performance across four key dimensions. Our findings demonstrate that the proposed architecture exhibits satisfactory performance in terms of generalization and employs an effective few-shot learning strategy. To explain further, Compared to the best results, the Pearson’s correlation coefficient (PCC) in the final stage increased by ~0.31%. Furthermore, we leverage the trained architecture to predict binding affinity scores of the DMS dataset of SARS-CoV-2 using transfer learning. Notably, training on a subset of the Ube4b dataset with 500 samples resulted in a notable improvement of 0.11 in the PCC. These results underscore the potential of our conceptual architecture as a promising methodology for multi-task protein function prediction.

[end paper 73]

[begin paper 74]

PMCID = 7791912

Title = Combination and tricombination therapy to destabilize the structural integrity of COVID-19 by some bioactive compounds with antiviral drugs: insights from molecular docking study

Recently, the SARS-CoV-2 (COVID-19) pandemic virus has been spreading throughout the world. Until now, no certified drugs have been discovered to efficiently inhibit the virus. The scientists are struggling to find new safe bioactive inhibitors of this deadly virus. In this study, we aim to find antagonists that may inhibit the activity of the three major viral targets: SARS-CoV-2 3-chymotrypsin-like protease (6LU7), SARS-CoV-2 spike protein (6VYB), and a host target human angiotensin-converting enzyme 2 (ACE2) receptor (1R42), which is the entry point for the viral encounter, were studied with the prospects of identifying significant drug candidate(s) against COVID-19 infection. Then, the protein stability produced score of less than 0.6 for all residues of all studied receptors. This confirmed that these receptors are extremely stable proteins, so it is very difficult to unstable the stability of these proteins through utilizing individual drugs. Hence, we studied the combination and tricombination therapy between bioactive compounds which have the best binding affinity and some antiviral drugs like chloroquine, hydroxychloroquine, azithromycin, simeprevir, baloxavir, lopinavir, and favipiravir to show the effect of combination and tricombination therapy to disrupt the stability of the three major viral targets that are mentioned previously. Also, ADMET study suggested that most of all studied bioactive compounds are safe and nontoxic compounds. All results confirmed that caulerpin can be utilized as a combination and tricombination therapy along with the studied antiviral drugs for disrupting the stability of the three major viral receptors (6LU7, 6VYB, and 1R42).

The online version contains supplementary material available at 10.1007/s11224-020-01723-5.

[end paper 74]

[begin paper 75]

PMCID = 9868522

Title = Prediction of antibody binding to SARS-CoV-2 RBDs

The ability to predict antibody–antigen binding is essential for computational models of antibody affinity maturation and protein design. While most models aim to predict binding for arbitrary antigens and antibodies, the global impact of SARS-CoV-2 on public health and the availability of associated data suggest that a SARS-CoV-2-specific model would be highly beneficial. In this work, we present a neural network model, trained on ∼315 000 datapoints from deep mutational scanning experiments, that predicts escape fractions of SARS-CoV-2 RBDs binding to arbitrary antibodies. The antibody embeddings within the model constitute an effective sequence space, which correlates with the Hamming distance, suggesting that these embeddings may be useful for downstream tasks such as binding prediction. Indeed, the model achieves Spearman correlation coefficients of 0.46 and 0.52 on two held-out test sets. By comparison, correlation coefficients calculated using existing structure and sequence-based models do not exceed 0.28. The correlation coefficient against dissociation constants of antibodies binding to SARS-CoV-2 RBD variants is 0.46. Additionally, the residue-level escapes are highest in the antibody epitope, correlating well with experimentally measured escapes. We further study the effect of antibody chain use, embedding dimension size and feed-forward and convolutional architectures on the model results. Lastly, we find that the inference time of our model is significantly faster than previous models, suggesting that it could be a useful tool for the accurate and rapid prediction of antibodies binding to SARS-CoV-2 RBDs.

The model and associated code are available for download at https://github.com/ericzwang/RBD_AB.

 Supplementary data are available at Bioinformatics Advances online.

[end paper 75]

[begin paper 76]

PMCID = 7541100

Title = An Assessment on Impact of COVID-19 Infection in a Gender Specific Manner

Coronavirus disease 2019 (COVID-19) is caused by novel coronavirus Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). It was first time reported in December 2019 in Wuhan, China and thereafter quickly spread across the globe. Till September 19, 2020, COVID-19 has spread to 216 countries and territories. Severe infection of SARS-CoV-2 cause extreme increase in inflammatory chemokines and cytokines that may lead to multi-organ damage and respiratory failure. Currently, no specific treatment and authorized vaccines are available for its treatment. Renin angiotensin system holds a promising role in human physiological system specifically in regulation of blood pressure and electrolyte and fluid balance. SARS-CoV-2 interacts with Renin angiotensin system by utilizing angiotensin-converting enzyme 2 (ACE2) as a receptor for its cellular entry. This interaction hampers the protective action of ACE2 in the cells and causes injuries to organs due to persistent angiotensin II (Ang-II) level. Patients with certain comorbidities like hypertension, diabetes, and cardiovascular disease are under the high risk of COVID-19 infection and mortality. Moreover, evidence obtained from several reports also suggests higher susceptibility of male patients for COVID-19 mortality and other acute viral infections compared to females. Analysis of severe acute respiratory syndrome coronavirus (SARS) and Middle East respiratory syndrome coronavirus (MERS) epidemiological data also indicate a gender-based preference in disease consequences. The current review addresses the possible mechanisms responsible for higher COVID-19 mortality among male patients. The major underlying aspects that was looked into includes smoking, genetic factors, and the impact of reproductive hormones on immune systems and inflammatory responses. Detailed investigations of this gender disparity could provide insight into the development of patient tailored therapeutic approach which would be helpful in improving the poor outcomes of COVID-19.

Graphical abstract

The online version of this article (10.1007/s12015-020-10048-z) contains supplementary material, which is available to authorized users.

[end paper 76]

[begin paper 77]

PMCID = 7476649

Title = Mesenchymal Stromal Cells in Viral Infections: Implications for COVID-19

Mesenchymal stromal cells (MSCs) constitute a heterogeneous population of stromal cells with immunomodulatory and regenerative properties that support their therapeutic use. MSCs isolated from many tissue sources replicate vigorously in vitro and maintain their main biological properties allowing their widespread clinical application. To date, most MSC-based preclinical and clinical trials targeted immune-mediated and inflammatory diseases. Nevertheless, MSCs have antiviral properties and have been used in the treatment of various viral infections in the last years. Here, we revised in detail the biological properties of MSCs and their preclinical and clinical applications in viral diseases, including the disease caused by the severe acute respiratory syndrome-coronavirus-2 (SARS-CoV-2) infection (COVID-19). Notably, rapidly increasing numbers of MSC-based therapies for COVID-19 have recently been reported. MSCs are theoretically capable of reducing inflammation and promote lung regeneration in severe COVID-19 patients. We critically discuss the rationale, advantages and disadvantages of MSC-based therapies for viral infections and also specifically for COVID-19 and point out some directions in this field. Finally, we argue that MSC-based therapy may be a promising therapeutic strategy for severe COVID-19 and other emergent respiratory tract viral infections, beyond the viral infection diseases in which MSCs have already been clinically applied.

Graphical Abstract

The online version of this article (10.1007/s12015-020-10032-7) contains supplementary material, which is available to authorized users.

[end paper 77]

[begin paper 78]

PMCID = 9909147

Title = Liposome-based high-throughput and point-of-care assays toward the quick, simple, and sensitive detection of neutralizing antibodies against SARS-CoV-2 in patient sera

The emergence of severe acute respiratory syndrome-related coronavirus 2 (SARS-CoV-2) in 2019 caused an increased interest in neutralizing antibody tests to determine the immune status of the population. Standard live-virus-based neutralization assays such as plaque-reduction assays or pseudovirus neutralization tests cannot be adapted to the point-of-care (POC). Accordingly, tests quantifying competitive binding inhibition of the angiotensin-converting enzyme 2 (ACE2) receptor to the receptor-binding domain (RBD) of SARS-CoV-2 by neutralizing antibodies have been developed. Here, we present a new platform using sulforhodamine B encapsulating liposomes decorated with RBD as foundation for the development of both a fluorescent, highly feasible high-throughput (HTS) and a POC-ready neutralizing antibody assay. RBD-conjugated liposomes are incubated with serum and subsequently immobilized in an ACE2-coated plate or mixed with biotinylated ACE2 and used in test strip with streptavidin test line, respectively. Polyclonal neutralizing human antibodies were shown to cause complete binding inhibition, while S309 and CR3022 human monoclonal antibodies only caused partial inhibition, proving the functionality of the assay. Both formats, the HTS and POC assay, were then tested using 20 sera containing varying titers of neutralizing antibodies, and a control panel of sera including prepandemic sera and reconvalescent sera from respiratory infections other than SARS-CoV-2. Both assays correlated well with a standard pseudovirus neutralization test (r = 0.847 for HTS and r = 0.614 for POC format). Furthermore, excellent correlation (r = 0.868) between HTS and POC formats was observed. The flexibility afforded by liposomes as signaling agents using different dyes and sizes can hence be utilized in the future for a broad range of multianalyte neutralizing antibody diagnostics.

The online version contains supplementary material available at 10.1007/s00216-023-04548-3.

[end paper 78]

[begin paper 79]

PMCID = 8445501

Title = Detection and evolution of SARS-CoV-2 coronavirus variants of concern with mass spectrometry

Mass mapping using high-resolution mass spectrometry has been applied to identify and rapidly distinguish SARS-CoV-2 coronavirus strains across five major variants of concern. Deletions or mutations within the surface spike protein across these variants, which originated in the UK, South Africa, Brazil and India (known as the alpha, beta, gamma and delta variants respectively), lead to associated mass differences in the mass maps. Peptides of unique mass have thus been determined that can be used to identify and distinguish the variants. The same mass map profiles are also utilized to construct phylogenetic trees, without the need for protein (or gene) sequences or their alignment, in order to chart and study viral evolution. The combined strategy offers advantages over conventional PCR-based gene-based approaches exploiting the ease with which protein mass maps can be generated and the speed and sensitivity of mass spectrometric analysis.

The online version contains supplementary material available at 10.1007/s00216-021-03649-1.

[end paper 79]

[begin paper 80]

PMCID = 8105700

Title = Analysis of natural compounds against the activity of SARS-CoV-2 NSP15 protein towards an effective treatment against COVID-19: a theoretical and computational biology approach

Coronavirus infectious disease 2019 (COVID-19), a viral infection caused by a novel coronavirus (nCoV), continues to emerge as a serious threat to public health. This pandemic caused by SARS-CoV-2 (severe acute respiratory syndrome–coronavirus-2) has infected globally with 1,550,000 plus deaths to date, representing a high risk to public health. No effective drug or vaccine is available to curb down this deadly virus. The expedition for searching for a potential drug or vaccine against COVID-19 is of massive potential and favour to the community. This study is focused on finding an effective natural compound that can be processed further into a potential inhibitor to check the activity of SARS-CoV-2 with minimal side effects targeting NSP15 protein, which belongs to the EndoU enzyme family. The natural screening suggested two efficient compounds (PubChem ID: 95372568 and 1776037) with dihydroxyphenyl region of the compound, found to be important in the interaction with the viral protein showing promising activity which may act as a potent lead inhibitory molecule against the virus. In combination with virtual screening, modelling, drug likeliness, molecular docking, and 500 ns cumulative molecular dynamics simulations (100 ns for each complex) along with the decomposition analysis to calculate and confirm the stability and fold, we propose 95372568 and 1776037 as novel compounds of natural origin capable of getting developed into potent lead molecules against SARS-CoV-2 target protein NSP15.

The online version contains supplementary material available at 10.1007/s00894-021-04750-z.

[end paper 80]

[begin paper 81]

PMCID = 10163859

Title = Persistent SARS-CoV-2 PCR Positivity Despite Anti-viral Treatment in Immunodeficient Patients

COVID-19 infection in immunodeficient individuals can result in chronically poor health, persistent or relapsing SARS-CoV-2 PCR positivity, and long-term infectious potential. While clinical trials have demonstrated promising outcomes using anti-SARS-CoV-2 medicines in immunocompetent hosts, their ability to achieve sustained viral clearance in immunodeficient patients remains unknown. We therefore aimed to study long-term virological outcomes in patients treated at our centre.

We followed up immunocompromised inpatients treated with casirivimab-imdevimab (Ronapreve) between September and December 2021, and immunocompromised patients who received sotrovimab, molnupiravir, nirmatrelvir/ritonavir (Paxlovid), or no treatment from December 2021 to March 2022. Nasopharyngeal swab and sputum samples were obtained either in hospital or in the community until sustained viral clearance, defined as 3 consecutive negative PCR samples, was achieved. Positive samples were sequenced and analysed for mutations of interest.

We observed sustained viral clearance in 71 of 103 patients, none of whom died. Of the 32/103 patients where sustained clearance was not confirmed, 6 died (between 2 and 34 days from treatment). Notably, we observed 25 cases of sputum positivity despite negative nasopharyngeal swab samples, as well as recurrence of SARS-CoV-2 positivity following a negative sample in 12 cases. Patients were then divided into those who cleared within 28 days and those with PCR positivity beyond 28 days. We noted lower B cell counts in the group with persistent PCR positivity (mean (SD) 0.06 (0.10) ×109/L vs 0.22 (0.28) ×109/L, p = 0.015) as well as lower IgA (median (IQR) 0.00 (0.00–0.15) g/L vs 0.40 (0.00–0.95) g/L, p = 0.001) and IgM (median (IQR) 0.05 (0.00–0.28) g/L vs 0.35 (0.10–1.10) g/L, p = 0.005). No differences were seen in CD4+ or CD8+ T cell counts. Antiviral treatment did not impact risk of persistent PCR positivity.

Persistent SARS-CoV-2 PCR positivity is common among immunodeficient individuals, especially those with antibody deficiencies, regardless of anti-viral treatment. Peripheral B cell count and serum IgA and IgM levels are predictors of viral persistence.

The online version contains supplementary material available at 10.1007/s10875-023-01504-9.

[end paper 81]

[begin paper 82]

PMCID = 7661101

Title = Development and evaluation of a serological test for diagnosis of COVID-19 with selected recombinant spike proteins

Serological test is a valuable diagnostic tool for coronavirus disease 2019 (COVID-19). However, considerable improvements to these tests are needed, especially in the detection sensitivity. In this study, six recombinant nucleocapsid and spike proteins of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) were prepared and evaluated, including three prokaryotic expression nucleocapsid proteins (rN, rN1, rN2) and three eukaryotic expression spike proteins (rS1, rS-RBD, rS-RBD-mFc). The recombinant proteins with the highest ELISA titers (rS1 and rS-RBD-mFc) were selected to develop a double-antigen sandwich colloidal gold immunochromatography assay (GICA) to detect total antibodies against SARS-CoV-2. The clinical evaluation results showed that the sensitivity and specificity of GICA were 92.09% (419/455) and 99.44% (706/710), respectively. Moreover, a significant number (65.63%, 21/32) of COVID-19 patients with undetectable viral RNA were correctly diagnosed by the GICA method. In conclusion, the eukaryotic expression spike proteins (rS1 and rS-RBD-mFc) are more suitable than the prokaryotic expression nucleocapsid proteins for serological diagnosis of SARS-CoV-2. The proposed GICA for detection of total antibodies could be a powerful complement to the current RNA tests for COVID-19.

The online version contains supplementary material available at 10.1007/s10096-020-04102-4.

[end paper 82]

[begin paper 83]

PMCID = 7657070

Title = Molecular basis for drug repurposing to study the interface of the S protein in SARS-CoV-2 and human ACE2 through docking, characterization, and molecular dynamics for natural drug candidates

A novel coronavirus (SARS-CoV-2) identified in Wuhan state of China in 2019 is the causative agent of deadly disease COVID-19. It has spread across the globe (more than 210 countries) within a short period. Coronaviruses pose serious health threats to both humans and animals. A recent publication reported an experimental 3D complex structure of the S protein of SARS-CoV-2 showed that the ectodomain of the SARS-CoV-2 S protein binds to the peptidase domain (PD) of human ACE2 with a dissociation constant (Kd) of ~ 15 nM. In this study, we focused on inhibitors for ACE2: S protein complex using virtual screening and inhibition studies through molecular docking for over 200,000 natural compounds. Toxicity analysis was also performed for the best hits, and the final complex structures for four complexes were subjected to 400 ns molecular dynamics simulations for stability testing. We found two natural origin inhibitors for the S protein: human ACE2 complex (Andrographolide and Pterostilbene) which displayed better inhibition potential for ACE2 receptor and its binding with the S protein of SARS-CoV-2. Comparative studies were also performed to test and verify that these two drug candidates are also better than hydroxychloroquine which is known to inhibit this complex. However, we needed better potential drug candidates to overcome the side effects of hydroxychloroquine. Supplementary experimental studies need to be carried forward to corroborate the viability of these two new inhibitors for ACE2: S protein complex so as to curb down COVID-19.

The online version contains supplementary material available at 10.1007/s00894-020-04599-8.

[end paper 83]

[begin paper 84]

PMCID = 7510013

Title = The Perfect Storm: COVID-19 Health Disparities in US Blacks

Coronavirus disease 2019 (COVID-19) accounts for over 180,000 deaths in the USA. Although COVID-19 affects all racial ethnicities, non-Hispanic Blacks have the highest mortality rates. Evidence continues to emerge, linking the disproportion of contagion and mortality from severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2), a result of adverse social determinants of health. Yet, genetic predisposition may also play a credible role in disease transmission. SARS-CoV-2 enters cells by interaction between SARS-CoV-2 spike protein and the receptor molecule angiotensin converting enzyme 2 (ACE2) expressed on the surface of the target cells, such that polymorphisms and the expression level of ACE2 influence infectivity and consequent pathogenesis of SARS-CoV-2. Genetic polymorphisms in other multiple genes, such as acetylcholinesterase (AChE) and interleukin-6, are also closely associated with underlying diseases, such as hypertension and type 2 diabetes mellitus, which substantially raise SARS-CoV-2 mortality. However, it is unknown how these genetic polymorphisms contribute to the disparate mortality rates, with or without underlying diseases. Of particular interest is the potential that genetic polymorphisms in these genes may be influencing the disparity of COVID-19 mortality rates in Black communities. Here, we review the evidence that biological predisposition for high-risk comorbid conditions may be relevant to our ability to fully understand and therefore address health disparities of COVID-19 deaths in Blacks.

The online version of this article (10.1007/s40615-020-00871-y) contains supplementary material, which is available to authorized users.

[end paper 84]

[begin paper 85]

PMCID = 7914120

Title = Structure-activity relationship (SAR) and molecular dynamics study of withaferin-A fragment derivatives as potential therapeutic lead against main protease (Mpro) of SARS-CoV-2

The spread of novel coronavirus SARS-CoV-2 has directed to a state of an unprecedented global pandemic. Many synthetic compounds and FDA-approved drugs have been significantly inhibitory against the virus, but no SARS-CoV-2 solution has been identified. However, small molecule fragment–based derivatives of potent phytocompounds may serve as promising inhibitors against SARS-CoV-2. In the pursuit of exploring novel SARS-CoV-2 inhibitors, we generated small molecule fragment derivatives from potent phytocompounds using neural networking and machine learning–based tools, which can cover unexplored regions of the chemical space that still retain lead-like properties. Out of 300 derivative molecules from withaferin-A, hesperidin, and baicalin, 30 were screened out with synthetic accessibility scores > 4 having the best ADME properties. The withaferin-A derivative molecules 61 and 64 exhibited a significant binding affinity of − 7.84 kcal/mol and − 7.94 kcal/mol. The docking study reveals that withaferin-A mol 61 forms 5 polar H-bonds with the Mpro where amino acids involved are GLU166, THR190, CYS145, MET165, and GLN152 and upon QSAR analysis showed a minimal predicted IC50 value of 7762.47 nM. Furthermore, the in silico cytotoxicity predictions, pharmacophore modeling, and molecular dynamics simulation studies have resulted in predicting the highly potent small molecule derivative from withaferin-A (phytocompound from Withania somnifera) to be the potential inhibitor of SARS-CoV 2 protease (Mpro) and a promising future lead candidate against COVID-19. The rationale of choosing withaferin-A from Withania somnifera (Ashwagandha) was propelled by the innumerous applications of Ashwagandha for the treatment of various antiviral diseases, common cold, and fever since time immemorial.

Graphical abstract

The online version contains supplementary material available at 10.1007/s00894-021-04703-6.

[end paper 85]

[begin paper 86]

PMCID = 7680993

Title = Probiotics-Derived Peptides and Their Immunomodulatory Molecules Can Play a Preventive Role Against Viral Diseases Including COVID-19

As of recent, the pandemic episode of COVID-19, a severe acute respiratory syndrome brought about by a novel coronavirus (SARS-CoV-2) expanding the pace of mortality, has affected the disease rate profoundly. Invulnerability is the fundamental choice to prevent the ruining event of COVID-19, as the drugs and antibodies are in the phase of preliminary clinical trials. Within this brief period, a few strains of SARS-CoV-2 have been recognized by the vaccine manufacturers, which could be an incorrect guess about the strain that will end up spreading. Since the circulating SARS-CoV-2 strains continue to mutate, immunizations, if at all works, might be for a restricted time. We have not put sufficient time in research to understand the immune responses that correlate with protection as this could help refine vaccines. Here, we have summed up the adequacy of the immunomodulatory component of probiotics for the prevention against viral infections. Furthermore, an in silico data have been provided in support of the “probiotics-derived lipopeptides” role in inactivating spike (S) glycoprotein of SARS-CoV-2 and its host receptor molecule, ACE2. Among well characterized lipopeptides derived from different probiotic strains, subtilisin (Bacillus amyloliquefaciens), curvacin A (Lactobacillus curvatus), sakacin P (Lactobacillus sakei), lactococcin Gb (Lactococcus lactis) was utilized in this study to demonstrate a higher binding proclivity to S-protein of SARS-CoV-2 and human ACE2. The outcome revealed noteworthy capabilities of the lipopeptides, due to their amphiphilic nature, to bind spike protein and receptor molecule, which may act to competitively inhibit the mandatory interaction of SARS-CoV-2 with the host epithelial cell expressing ACE2 for its entry into the cell for reproduction. In the current situation, probiotic treatment alongside chemotherapy may assist in bringing about substantial improvement of the health of COVID-19 patients. At the same time, probiotics may aid towards building up the immune defenses in people to evade COVID-19.

The online version contains supplementary material available at 10.1007/s12602-020-09727-7.

[end paper 86]

[begin paper 87]

PMCID = 9066385

Title = Artificial Neural Network-Based Study Predicts GS-441524 as a Potential Inhibitor of SARS-CoV-2 Activator Protein Furin: a Polypharmacology Approach

Furin, a pro-protein convertase, plays a significant role as a biological scissor in bacterial, viral, and even mammalian substrates which in turn decides the fate of many viral and bacterial infections along with the numerous ailments caused by cancer, diabetes, inflammations, and neurological disorders. In the wake of the current pandemic caused by the virus SARS-CoV-2, furin has become the center of attraction for researchers as the spike protein contains a polybasic furin cleavage site. In the present work, we have searched for novel inhibitors against this interesting human target from FDA-approved antiviral. To enhance the selection of new inhibitors, we employed Kohonen’s artificial neural network-based self-organizing maps for ligand-based virtual screening. Promising results were obtained which can help in drug repurposing and network pharmacology studies can address the errors generated due to promiscuity/polypharmacology. We found 15 existing FDA antiviral drugs having the potential to inhibit furin. Among these, six compounds have targets on important human proteins (LDLR, FCGR1A, PCK1, TLR7, DNA, and PNP). The role of these 15 drugs inhibiting furin can be established by studying further on patients infected with number of viruses including SARS-CoV-2. Here we propose two promising candidate FDA drugs GS-441524 and Grazoprevir (MK-5172) for repurposing as inhibitors of furin. The best results were observed with GS-441524.

The online version contains supplementary material available at 10.1007/s12010-022-03928-2.

[end paper 87]

[begin paper 88]

PMCID = 8390178

Title = The opportunity cost of automated glycopeptide analysis: case study profiling the SARS-CoV-2 S glycoprotein

Glycosylation analysis of viral glycoproteins contributes significantly to vaccine design and development. Among other benefits, glycosylation analysis allows vaccine developers to assess the impact of construct design or producer cell line choices for vaccine production, and it is a key measure by which glycoproteins that are produced for use in vaccination can be compared to their native viral forms. Because many viral glycoproteins are multiply glycosylated, glycopeptide analysis is a preferrable approach for mapping the glycans, yet the analysis of glycopeptide data can be cumbersome and requires the expertise of an experienced analyst. In recent years, a commercial software product, Byonic, has been implemented in several instances to facilitate glycopeptide analysis on viral glycoproteins and other glycoproteomics data sets, and the purpose of the study herein is to determine the strengths and limitations of using this software, particularly in cases relevant to vaccine development. The glycopeptides from a recombinantly expressed trimeric S glycoprotein of the SARS-CoV-2 virus were first analyzed using an expert-based analysis strategy; subsequently, analysis of the same data set was completed using Byonic. Careful assessment of instances where the two methods produced different results revealed that the glycopeptide assignments from Byonic contained more false positives than true positives, even when the data were assessed using a 1% false discovery rate. The work herein provides a roadmap for removing the spurious assignments that Byonic generates, and it provides an assessment of the opportunity cost for relying on automated assignments for glycopeptide data sets from viral glycoproteins.

The online version contains supplementary material available at 10.1007/s00216-021-03621-z.

[end paper 88]

[begin paper 89]

PMCID = 9898852

Title = SARS-CoV-2 epidemiological trend before vaccination era: a seroprevalence study in Apulia, Southern Italy, in 2020

The present study aimed at assessing the prevalence of antibodies against SARS-CoV-2 in the general population in the province of Bari (Apulia region, Southern Italy) during the year 2020.

In this study, 1325 serum samples collected from January to December 2020 were tested for the presence of IgM and IgG antibodies against whole-virus SARS-CoV-2 antigen by commercial ELISA. Positive samples were further tested by in-house ELISA for the detection of anti-receptor binding domain (RBD) IgM and IgG antibodies and by micro-neutralization (MN) assay for the detection of neutralizing antibody.

One hundred (7.55%) samples had the presence of at least one antibody class against SARS-CoV-2 by commercial ELISA, of which 88 (6.6%) showed IgG and 19 (1.4%) showed IgM antibodies. The proportion of samples with IgG antibodies increased from 1.9% in January–February to 9.6% in November–December, while no significant increase was observed for IgM. When tested by in-house ELISA and MN assay, 17.0% and 31.6% were found positive to RBD IgG and RBD IgM, respectively, while 12.0% showed neutralizing antibody.

The proportion of samples with SARS-CoV-2 IgG antibodies increased during 2020, especially in the second half of the year, consistent with data reported by the routine epidemiological surveillance of SARS-CoV-2 cases. Despite the high number of reported cases, the seroprevalence values are relatively low, and only a small proportion of samples had neutralizing antibodies.

The online version contains supplementary material available at 10.1007/s10389-023-01834-3.

[end paper 89]

[begin paper 90]

PMCID = 8369332

Title = Deep survey for designing a vaccine against SARS-CoV-2 and its new mutations

The ongoing global pandemic caused by severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) has prompted worldwide vaccine development. Several vaccines have been authorized by WHO, FDA, or MOH of different countries. However, issues such as need for cold chain, price, and most importantly access problems have limited vaccine usage in some nations especially developing countries. Moreover, the vast global demand justifies further attempts for vaccine development. Multi-epitope polypeptide vaccines enjoy several key features including safety and lower production and transfer costs and could be designed by in silico tools. Spike protein (S), membrane protein (M), and nucleocapsid protein (N), the three major structural proteins of SARS-CoV-2, are ideal candidates for epitope selection. ORF3a (open reading frame3a), a transmembrane protein with pro-apoptotic functions, could be another proper target. Thus, a novel multi-epitope vaccine against SARS-CoV-2 was designed using these four proteins and LL37, a TLR3 agonist adjuvant, through different immunoinformatics and bioinformatics tools. The proposed multi-epitope vaccine is expected to induce robust humoral and cellular immune responses against SARS-CoV-2 with a population coverage of 76.92 % due to containing different immunodominant epitopes and LL37 adjuvant. Selecting epitopes derived from one functional and three structural proteins suggests the protective ability of the vaccine irrespective of probable virus mutations. The computationally observed proper interaction of LL37 with TLR3 implies its ability to induce immune responses effectively. Besides, it showed acceptable structural and physicochemical properties. The in-silico cloning results predicted its high efficiency production in Escherichia coli. Future experimental studies could further confirm its immunological efficacy.

The online version contains supplementary material available at 10.1007/s11756-021-00866-y.

[end paper 90]

[begin paper 91]

PMCID = 7481766

Title = Renin-Angiotensin System Inhibitors and COVID-19: a Systematic Review and Meta-Analysis. Evidence for Significant Geographical Disparities

While the COVID-19 pandemic is constantly evolving, it remains unclear whether the use of angiotensin-converting enzyme (ACE) inhibitors or angiotensin receptor blockers (ARBs) affects the clinical course of SARS-CoV-2 infection. For this meta-analysis, PubMed, CENTRAL, and grey literature were searched from their inception to 19 May 2020 for randomized, controlled trials or observational studies that evaluate the association between the use of either ACE inhibitors or ARBs and the risk for major clinical endpoints (infection, hospitalization, admission to ICU, death) in adult patients during the COVID-19 pandemic. In addition, a subgroup geographical analysis of outcomes was performed. Studies including less than 100 subjects were excluded from our analysis.

In total, 25 observational studies were included. ACE inhibitors and ARBs were not associated with increased odds for SARS-CoV-2 infection, admission to hospital, severe or critical illness, admission to ICU, and SARS-CoV-2-related death. In Asian countries, the use of ACE inhibitors/ARBs decreased the odds for severe or critical illness and death (OR = 0.37, 95% CI 0.16–0.89, I2 = 83%, and OR = 0.62, 95% CI 0.39–0.99, I2 = 0%, respectively), whereas they increased the odds for ICU admission in North America and death in Europe (OR = 1.75, 95% CI 1.37–2.23, I2 = 0%, and OR = 1.68, 95% CI 1.05–2.70, I2 = 82%, respectively). ACE inhibitors might be marginally protective regarding SARS-CoV-2-related death compared with ARBs (OR = 0.86, 95% CI 0.74–1.00, I2 = 0%).

Randomized controlled trials are needed to confirm the aforementioned associations between ACE inhibitors, ARBs, and SARS-CoV-2.

The online version of this article (10.1007/s11906-020-01101-w) contains supplementary material, which is available to authorized users.

[end paper 91]

[begin paper 92]

PMCID = 10176293

Title = Marine drugs as putative inhibitors against non-structural proteins of SARS-CoV-2: an in silico study

Coronavirus disease 2019 (COVID-19) is an unprecedented pandemic, threatening human health worldwide. The need to produce novel small-molecule inhibitors against the ongoing pandemic has resulted in the use of drugs such as chloroquine, azithromycin, dexamethasone, favipiravir, ribavirin, remdesivir and azithromycin. Moreover, the reports of the clinical trials of these drugs proved to produce detrimental effects on patients with side effects like nephrotoxicity, retinopathy, cardiotoxicity and cardiomyopathy. Recognizing the need for effective and non-harmful therapeutic candidates to combat COVID-19, we aimed to develop promising drugs against SARS-COV-2.

In the current investigation, high-throughput virtual screening was performed using the Comprehensive Marine Natural Products Database against five non-structural proteins: Nsp3, Nsp5, Nsp12, Nsp13 and Nsp15. Furthermore, standard precision (SP) docking, extra precision (XP) docking, binding free energy calculation and absorption, distribution, metabolism, excretion and toxicity studies were performed using the Schrӧdinger suite. The top-ranked 5 hits obtained by computational studies exhibited to possess a greater binding affinity with the selected non-structural proteins. Amongst the five hits, CMNPD5804, CMNPD20924 and CMNPD1598 hits were utilized to design a novel molecule (D) that has the capability of interacting with all the key residues in the pocket of the selected non-structural proteins. Furthermore, 200 ns of molecular dynamics simulation studies provided insight into the binding modes of D within the catalytic pocket of selected proteins.

Hence, it is concluded that compound D could be a promising inhibitor against these non-structural proteins. Nevertheless, there is still a need to conduct in vitro and in vivo studies to support our findings.

The online version contains supplementary material available at 10.1007/s00894-023-05574-9.

[end paper 92]

[begin paper 93]

PMCID = 8301390

Title = Expression of SARS-CoV-2 Entry Factors in Human Alveolar Type II Cells in Aging and Emphysema

Alveolar type II (ATII) cells proliferate and restore the injured epithelium. It has been described that SARS-CoV-2 infection causes diffuse alveolar damage in the lungs. However, host factors facilitating virus infection in ATII cells are not well known. We determined the SARS-CoV-2-related genes and protein expression using RT-PCR and Western blotting, respectively, in ATII cells isolated from young and elderly non-smokers, smokers, and ex-smokers. Cells were also obtained from lung transplants of emphysema patients. ACE2 has been identified as the receptor for SARS-CoV-2, and we found significantly increased levels in young and elderly smokers and emphysema patients. The viral entry depends on TMPRSS2 protease activity, and a higher expression was detected in elderly smokers and ex-smokers and emphysema patients. Both ACE2 and TMPRSS2 mRNA levels were higher in this disease in comparison with non-smokers. CD209L serves as a receptor for SARS-CoV-2, and we found increased levels in ATII cells obtained from smokers and in emphysema patients. Also, our data suggest CD209L regulation by miR142. Endoplasmic reticulum stress was detected in ATII cells in this disease. Our results suggest that upregulation of SARS-CoV-2 entry factors in ATII cells in aging, smokers, and emphysema patients may facilitate infection.

[end paper 93]

[begin paper 94]

PMCID = 11614202

Title = Prediction of virus-host associations using protein language models and multiple instance learning

Predicting virus-host associations is essential to determine the specific host species that viruses interact with, and discover if new viruses infect humans and animals. Currently, the host of the majority of viruses is unknown, particularly in microbiomes. To address this challenge, we introduce EvoMIL, a deep learning method that predicts the host species for viruses from viral sequences only. It also identifies important viral proteins that significantly contribute to host prediction. The method combines a pre-trained large protein language model (ESM) and attention-based multiple instance learning to allow protein-orientated predictions. Our results show that protein embeddings capture stronger predictive signals than sequence composition features, including amino acids, physiochemical properties, and DNA k-mers. In multi-host prediction tasks, EvoMIL achieves median F1 score improvements of 10.8%, 16.2%, and 4.9% in prokaryotic hosts, and 1.7%, 6.6% and 11.5% in eukaryotic hosts. EvoMIL binary classifiers achieve impressive AUC over 0.95 for all prokaryotic hosts and range from roughly 0.8 to 0.9 for eukaryotic hosts. Furthermore, EvoMIL identifies important proteins in the prediction task, capturing key functions involved in virus-host specificity.

Being able to predict which viruses can infect which host species, and identifying the specific proteins that are involved in these interactions, are fundamental tasks in virology. Traditional methods for predicting these interactions rely on identifying common features among proteins, overlooking the structure of the protein “language” encoded in individual proteins. We have developed a novel method that combines a protein language model and multiple instance learning to allow host prediction directly from protein sequences, without the need to extract features manually. This method significantly improved prediction accuracy and revealed key proteins involved in virus-host interactions.

[end paper 94]

[begin paper 95]

PMCID = 8248955

Title = Macrolactin A as a Novel Inhibitory Agent for SARS-CoV-2 Mpro: Bioinformatics Approach

COVID-19 is a disease that puts most of the world on lockdown and the search for therapeutic drugs is still ongoing. Therefore, this study used in silico screening to identify natural bioactive compounds from fruits, herbaceous plants, and marine invertebrates that are able to inhibit protease activity in SARS-CoV-2 (PDB: 6LU7). We have used extensive screening strategies such as drug likeliness, antiviral activity value prediction, molecular docking, ADME, molecular dynamics (MD) simulation, and MM/GBSA. A total of 17 compounds were shortlisted using Lipinski’s rule in which 5 compounds showed significant predicted antiviral activity values. Among these 5, only 2 compounds, Macrolactin A and Stachyflin, showed good binding energy of −9.22 and −8.00 kcal/mol, respectively, within the binding pocket of the Mpro catalytic residues (HIS 41 and CYS 145). These two compounds were further analyzed to determine their ADME properties. The ADME evaluation of these 2 compounds suggested that they could be effective in developing therapeutic drugs to be used in clinical trials. MD simulations showed that protein–ligand complexes of Macrolactin A and Stachyflin with the target receptor (6LU7) were stable for 100 nanoseconds. The MM/GBSA calculations of Mpro–Macrolactin A complex indicated higher binding free energy (−42.58 ± 6.35 kcal/mol). Dynamic cross-correlation matrix (DCCM) and principal component analysis (PCA) on the residual movement in the MD trajectories further confirmed the stability of Macrolactin A bound state with 6LU7. In conclusion, this study showed that marine natural compound Macrolactin A could be an effective therapeutic inhibitor against SARS-CoV-2 protease (6LU7). Additional in vitro and in vivo validations are strongly needed to determine the efficacy and therapeutic dose of Macrolactin A in biological systems.

The online version contains supplementary material available at 10.1007/s12010-021-03608-7.

[end paper 95]

[begin paper 96]

PMCID = 7844105

Title = Strong Binding of Leupeptin with TMPRSS2 Protease May Be an Alternative to Camostat and Nafamostat for SARS-CoV-2 Repurposed Drug: Evaluation from Molecular Docking and Molecular Dynamics Simulations

The unprecedented coronavirus SARS-CoV-2 outbreak at Wuhan, China, caused acute respiratory infection to humans. There is no precise vaccine/therapeutic agents available to combat the COVID-19 disease. Some repurposed drugs are saving the life of diseased, but the complete cure is relatively less. Several drug targets have been reported to inhibit the SARS-CoV-2 virus infection, in that TMPRSS2 (transmembrane protease serine 2) is one of the potential targets; inhibiting this protease stops the virus entry into the host human cell. Camostat mesylate, nafamostat, and leupeptin are the drugs, in which the first two drugs are being used for COVID-19 and leupeptin also tested. To consider these drugs as the repurposed drug for COVID-19, it is essential to understand their binding affinity and stability with TMPRSS2. In the present study, we performed the molecular docking and molecular dynamics (MD) simulation of these molecules with the TMPRSS2. The docking study reveals that leupeptin molecule strongly binds with TMPRSS2 protein than the other two drug molecules. The RMSD and RMSF values of MD simulation confirm that leupeptin and the amino acids of TMPRSS2 are very stable than the other two molecules. Furthermore, leupeptin forms interactions with the key amino acids of TMPRSS2 and the same have been maintained during the MD simulations. This structural and dynamical information is useful to evaluate these drugs to be used as repurposed drugs, however, the strong binding profile of leupeptin with TMPRSS2, suggests, it may be considered as a repurposed drug for COVID-19 disease after clinical trial.

The online version contains supplementary material available at 10.1007/s12010-020-03475-8.

[end paper 96]

[begin paper 97]

PMCID = 8419828

Title = Computational approach towards the design of artemisinin–thymoquinone hybrids against main protease of SARS-COV-2

The sanitary emergency installed in the world, generated by the pandemic of COVID-19, instigates the search for scientific strategies to mitigate the damage caused by the disease to different sectors of society. The disease caused by the coronavirus, SARS-CoV-2, reached 216 countries/territories, where about 199 million people were reported with the infection. Of these, more than 4 million died. In this sense, strategies involving the development of new antiviral molecules are extremely important. The main protease (Mpro) from SARS-CoV-2 is an important target, which has been widely studied for antiviral treatment. This work aims to perform a screening of pharmacodynamics and pharmacokinetics of synthetic hybrids from thymoquinone and artemisin (THY-ART) against COVID-19.

Molecular docking studies indicated that hybrids of artemisinin and thymoquinone showed a relevant interaction with the active fraction of the enzyme Mpro, when compared to the reference drugs. Furthermore, hybrids show an improvement in the interaction of substances with the enzyme, mainly due to the higher frequency of interactions with the Thr199 residue. ADMET studies indicated that hybrids tend to permeate biological membranes, allowing good human intestinal absorption, with low partition to the central nervous system, potentiation for CYP-450 enzyme inhibitors, low risk of toxicity compared to commercially available drugs, considering mainly mutagenicity and cardiotoxicity, low capacity of hybrids to permeate the blood–brain barrier, high absorption and moderate permeability in Caco-2 cells. In addition, T1–T7 tend to have a better distribution of their available fractions to carry out diffusion and transport across cell membranes, as well as increase the energy of interaction with the SARS-CoV-2 target.

Hybrid products of artemisinin and thymoquinone have the potential to inhibit Mpro, with desirable pharmacokinetic and toxicity characteristics compared to commercially available drugs, being indicated for preclinical and subsequent clinical studies against SARS-CoV-2. Emphasizing the possibility of synergistic use with currently used drugs in order to increase half-life and generate a possible synergistic effect. This work represents an important step for the development of specific drugs against COVID-19.

[end paper 97]

[begin paper 98]

PMCID = 8102132

Title = Process development and scale-up optimization of the SARS-CoV-2 receptor binding domain–based vaccine candidate, RBD219-N1C1

A SARS-CoV-2 RBD219-N1C1 (RBD219-N1C1) recombinant protein antigen formulated on Alhydrogel® has recently been shown to elicit a robust neutralizing antibody response against SARS-CoV-2 pseudovirus in mice. The antigen has been produced under current good manufacturing practices (cGMPs) and is now in clinical testing. Here, we report on process development and scale-up optimization for upstream fermentation and downstream purification of the antigen. This includes production at the 1-L and 5-L scales in the yeast, Pichia pastoris, and the comparison of three different chromatographic purification methods. This culminated in the selection of a process to produce RBD219-N1C1 with a yield of >400 mg per liter of fermentation with >92% purity and >39% target product recovery after purification. In addition, we show the results from analytical studies, including SEC-HPLC, DLS, and an ACE2 receptor binding assay that were performed to characterize the purified proteins to select the best purification process. Finally, we propose an optimized upstream fermentation and downstream purification process that generates quality RBD219-N1C1 protein antigen and is fully scalable at a low cost.

• Yeast fermentation conditions for a recombinant COVID-19 vaccine were determined.

• Three purification protocols for a COVID-19 vaccine antigen were compared.

• Reproducibility of a scalable, low-cost process for a COVID-19 vaccine was shown.

Graphical abstract 

The online version contains supplementary material available at 10.1007/s00253-021-11281-3.

[end paper 98]

[begin paper 99]

PMCID = 10997877

Title = Databases of ligand-binding pockets and protein-ligand interactions

Many research groups and institutions have created a variety of databases curating experimental and predicted data related to protein-ligand binding. The landscape of available databases is dynamic, with new databases emerging and established databases becoming defunct. Here, we review the current state of databases that contain binding pockets and protein-ligand binding interactions. We have compiled a list of such databases, fifty-three of which are currently available for use. We discuss variation in how binding pockets are defined and summarize pocket-finding methods. We organize the fifty-three databases into subgroups based on goals and contents, and describe standard use cases. We also illustrate that pockets within the same protein are characterized differently across different databases. Finally, we assess critical issues of sustainability, accessibility and redundancy.

[end paper 99]

[begin paper 100]

PMCID = 8553591

Title = Histopathological assessments reveal retinal vascular changes, inflammation, and gliosis in patients with lethal COVID-19

The purpose of this study is to assess for histopathological changes within the retina and the choroid and determine the long-term sequelae of the SARS-CoV-2 infection.

Eyes from seven COVID-19-positive and six similar age-matched control donors with a negative test for SARS-CoV-2 were assessed. Globes were evaluated ex vivo with macroscopic, SLO and OCT imaging. Macula and peripheral regions were processed for Epon embedding and immunocytochemistry.

Fundus analysis shows hemorrhagic spots and increased vitreous debris in several of the COVID-19 eyes compared to the controls. OCT-based measurements indicated an increased trend in retinal thickness in the COVID-19 eyes; however, the difference was not statistically significant. Histology of the retina showed presence of hemorrhages and central cystoid degeneration in several of the donors. Whole mount analysis of the retina labeled with markers showed changes in retinal microvasculature, increased inflammation, and gliosis in the COVID-19 eyes compared to the controls. The choroidal vasculature displayed localized changes in density and signs of increased inflammation in the COVID-19 samples.

In situ analysis of the retinal tissue suggests that there are severe subclinical abnormalities that could be detected in the COVID-19 eyes. This study provides a rationale for evaluating the ocular physiology of patients that have recovered from COVID-19 infections to further understand the long-term effects caused by this virus.

The online version contains supplementary material available at 10.1007/s00417-021-05460-1.

[end paper 100]



