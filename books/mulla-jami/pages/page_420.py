# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 420 (printed ٤١٩)."""

PAGE_NUMBER = 420
PRINTED_PAGE = "٤١٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وأشار بترتيبها في الذكر إلى ترتيبها» from PDF p. 419.
    {"type": "matn",
     "ar": "بحسب المرتبة[[١]]:",
     "en": "…in rank:"},
    {"type": "matn",
     "ar": "فالأول: (المضمرات) فإنها موضوعة[[٢]] بإزاء معان معينة مشخصة باعتبار أمر كلي،",
     "en": "The first is (the pronouns (muḍmarāt)), for they are coined for determinate, individuated meanings by way of a universal notion:"},
    {"type": "matn",
     "ar": "فإن الواضع لاحظ أولا مفهوم المتكلم الواحد من حيث إنه يحكي عن نفسه مثلا، وجعله آلة لملاحظة أفراده،",
     "en": "the coiner first considered the concept of the single speaker insofar as he speaks of himself, for example, and made it an instrument for considering its individuals;"},
    {"type": "matn",
     "ar": "ووضع لفظ «أنا» بإزاء كل واحد من تلك الأفراد بخصوصه، بحيث لا يفاد ولا يفهم إلا واحد بخصوصه دون القدر المشترك،",
     "en": "and he coined the word “anā” (I) for each one of those individuals in its particularity, such that only one individual in its particularity is conveyed and understood, not the shared measure."},
    {"type": "matn",
     "ar": "فيتعقل ذلك المشترك آلة للوضع، لا أنه الموضوع له، فالوضع كلي والموضوع له جزئي مشخص[[٣]].",
     "en": "That shared [concept] is conceived as an instrument of the coinage, not as what is coined for; so the coinage is universal and what is coined for is a particular, individuated thing."},
    {"type": "matn",
     "ar": "(و) الثاني: (الأعلام) المشخصة، كما إذا تصور ذات «زيد» ووضع لفظ «زيد» بإزائه من حيث معلوميته ومعهوديته[[٤]]",
     "en": "(And) the second is (proper names (aʿlām)): individual ones, as when the essence of “Zayd” is conceived and the word “Zayd” is coined for it insofar as it is known and familiar;"},
    {"type": "matn",
     "ar": "أو الجنسية، كما إذا تصور مفهوم «الأسد» وهو الحيوان المفترس، ووضع بإزائه من حيث معلوميته ومعهوديته لفظ «أسامة»،",
     "en": "or generic ones, as when the concept of “the lion”—the predatory animal—is conceived and the word “usāma” is coined for it insofar as it is known and familiar."},
    {"type": "matn",
     "ar": "فهذا اللفظ بهذا الاعتبار علم لهذا المعنى الجنسي ومعرفة،",
     "en": "In this respect this word is a proper name for this generic meaning, and definite;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا وضع لفظ «الأسد» بإزاء هذا المفهوم الجنسي مع قطع النظر عن معلوميته ومعهوديته، فإنه بهذا الاعتبار نكرة.",
     "en": "unlike when the word “asad” is coined for this generic concept without regard to its being known and familiar, for in this respect it is indefinite."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «فإن المهمات» printed so (expected المبهمات, the demonstratives); transcribed as printed.
    {"type": "pair",
     "ar": "تبع في ذلك الهندي، وليس بذاك، فإن المهمات منها ما يساوي ذا اللام والمضاف إلى أحدها معنى",
     "en": "In this he followed al-Hindī, and it is not sound; for among the demonstratives (mubhamāt) is what equals in meaning the noun with the article and the noun annexed to one of them;"},
    {"type": "pair",
     "ar": "منه ما يساوي المعرف باللام ومنه ما يفرقه.",
     "en": "of [the latter], some equals the noun made definite by the article and some exceeds it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا على رأي المحققين المتأخرين.",
     "en": "This is according to the view of the later verifying scholars (muḥaqqiqūn)."},
    {"type": "pair",
     "ar": "وأما على رأي المتقدمين فهي موضوعة لمعان كلية بشرط استعمالها في جزئياتها، فالمعنى الحقيقي مهجور بالكلية.",
     "en": "According to the view of the earlier scholars, they are coined for universal meanings on condition of being used for their particulars, so that the literal meaning is entirely abandoned."},
    {"type": "pair",
     "ar": "وكذا الاختلاف في المبهمات والحروف.",
     "en": "The same disagreement holds for demonstratives and particles."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كان ينبغي الاكتفاء بالجزئي؛ لأن التحقيق أن الموضوع له جزئي إضافي فربما يكون كليا،",
     "en": "He should have been content with “particular”, because the verified view is that what is coined for is a relative particular, and so may be universal."},
    {"type": "pair",
     "ar": "ومما ينبغي أن يعلم أن الوضع الكلي للموضوع له الجزئي مما فاز به بعض محقق المتأخرين والقدماء لم يعثروا عليه حتى المصنف،",
     "en": "Among what should be known is that universal coinage for a particular thing coined for is something attained by some verifying later scholar, and the ancients did not come upon it, including the author;"},
    {"type": "pair",
     "ar": "فيجعل معنى قوله: لشيء بعينه لإفادة شيء بعينه.",
     "en": "so the meaning of his words “for a thing in its specificity” is taken to be “to convey a thing in its specificity”."},
    # REVIEW: «وقال الواضع» printed so; transcribed as printed.
    {"type": "pair",
     "ar": "وقال الواضع: وضع المضمر مثلا لمفهوم كلي ليستعمل في جزئي من جزئياته، وشرط ألا يستعمل في مفهومه الكلي، فمفهومه الكلي مهجور في الاستعمال،",
     "en": "The coiner said: the pronoun, for example, was coined for a universal concept to be used for one of its particulars, with the condition that it not be used for its universal concept; so its universal concept is abandoned in usage."},
    {"type": "pair",
     "ar": "واللام في قوله: لشيء ليس صلة الوضع بل غرضية،",
     "en": "The lām in his words “for a thing” is not the complement of the coinage but expresses purpose."},
    {"type": "pair",
     "ar": "والشارح لما رأى إمكان تطبيق عبارته على ما هو الحق شرحه به تعليما لما هو الحق، ولم يلتفت إلى ما قصده به.",
     "en": "When the commentator saw that his wording could be fitted to what is true, he explained it accordingly, to teach what is true, and paid no attention to what [the author] intended by it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يتبادر منه لسابق كلامه المعهودية في ذهن المتكلم والمخاطب، والتحقيق ما عرفت، فلا تنس وكن من المتذكرين.",
     "en": "From it, owing to his earlier words, familiarity in the mind of the speaker and the addressee comes to mind first; the verified view is what you have learned, so do not forget, and be among those who remember."},
    {"type": "pair",
     "ar": "ويشكل تصوير العلم الشخصي بأنه الذي تصور الذات بعينه، ووضع بإزائه بلفظ الله،",
     "en": "Depicting the individual proper name as one where the essence is conceived in its specificity and [a word] coined for it is problematic in the case of the word “Allāh”,"},
    {"type": "pair",
     "ar": "فإنه لم يقع تصوره تعالى لغيره بشخصه، فلا يمكن وضعه إن كان الواضع غيره،",
     "en": "for the Exalted has not been conceived by anyone other than Him in His individual self, so its coinage is impossible if the coiner is other than Him;"},
    {"type": "pair",
     "ar": "وإن كان الواضع إياه فلا يمكن معرفة وضعه لغيره حتى يترتب فائدة الوضع العلمي، وهو فهم الشخص بعينه،",
     "en": "and if the coiner is He, then others cannot know its coinage, so that the benefit of proper-name coinage—understanding the individual in its specificity—would follow."},
    {"type": "pair",
     "ar": "ويشكل بوضع الآباء الأعلام لأبنائهم في غيبة الأبناء قبل رؤيتهم،",
     "en": "It is also problematic in the case of fathers coining names for their sons in the sons’ absence, before seeing them;"},
    {"type": "pair",
     "ar": "وبوضع العلم للشخص مع أنه يتبدل تشخصاته من أول عمره إلى آخره يوما فيوما، فلم يتصور مسمى علم بشخصه حين وضع العلم للمشخص،",
     "en": "and in the case of coining a proper name for an individual even though his individuating features change day by day from the beginning of his life to its end, so that what a proper name names is not conceived in its individuality when the name is coined for the individual;"},
    {"type": "pair",
     "ar": "فإنه موضوع بمشخصاته المتبدلة من أول عمره إلى آخره، فلا يمكن تصوره بخصوصه الذي وضع اللفظ له بهذا الخصوص.",
     "en": "for it is coined [for him] with his changing individuating features from the beginning of his life to its end, so he cannot be conceived in the particularity for which the word was coined with this particularity."},
]
