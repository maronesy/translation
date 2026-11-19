# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 38 (printed ٣٧)."""

PAGE_NUMBER = 38
PRINTED_PAGE = "٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "وتخصيص أصلا، وبقيت حروف الهجاء[[١]] الموضوعة لغرض التركيب لا بإزاء المعنى، وخرجت[[٢]] بقوله: «لمعنى»؛ إذ وضعها لغرض التركيب لا بإزاء المعنى.",
     "en": "…nor any specification (takhṣīṣ) at all. There remain the letters of the alphabet (ḥurūf al-hijāʾ), which are posited for the purpose of composition (tarkīb) and not to correspond to a meaning; these are excluded by his words “li-maʿnā” (for a meaning), since they are posited for the purpose of composition, not to correspond to a meaning."},
    {"type": "matn",
     "ar": "فإن قلت: قد وضع بعض الألفاظ بإزاء بعض آخر[[٣]]، فكيف يصدق عليه[[٤]] أنه[[٥]] وضع لمعنى[[٦]]؟",
     "en": "If you say: some expressions have been posited to correspond to certain other [expressions]; how, then, does it hold true of it that it is a positing for a meaning?"},
    {"type": "matn",
     "ar": "قلنا: المعنى ما يتعلق به القصد[[٧]]، وهو أعم من أن يكون لفظا أو غيره.",
     "en": "We say: meaning is that to which the intention attaches, and this is more general than being either a wording or something else."},
    {"type": "matn",
     "ar": "فإن قلت: قد وضع بعض الكلمات[[٨]] بإزاء الألفاظ المركبة، كلفظ «الجملة» و«الخبر»، فكيف يكون موضوعا لمفرد[[٩]]؟",
     "en": "If you say: some words have been posited to correspond to compound expressions, like the words “al-jumla” (the sentence) and “al-khabar” (the predicate); how, then, can it be posited for a singular (mufrad)?"},
    {"type": "matn",
     "ar": "قلنا: هذه الألفاظ وإن كانت بالقياس إلى معانيها مركبة، لكنها[[١٠]] بالقياس إلى ألفاظها الموضوعة بإزائها مفردة.",
     "en": "We say: these expressions, though compound in relation to their meanings, are nonetheless singular in relation to the expressions posited to correspond to them."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: حروف تعدد بأساميها كألف، باء، تاء، وهي حروف المباني المقابلة لحروف المعاني.",
     "en": "That is: letters that are enumerated by their names, like alif, bāʾ, tāʾ; they are the letters of structure (ḥurūf al-mabānī), as opposed to the particles of meaning (ḥurūf al-maʿānī)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الحروف المذكورة.",
     "en": "[That is:] the aforementioned letters."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى: قد وضع بعض الكلمات بإزاء بعض آخر، ليتضح فساد التعريف لعدم صدقه عليه.",
     "en": "The better [wording is]: “some words have been posited to correspond to certain others,” so that the defectiveness of the definition may become evident, owing to its not holding true of it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: على ذلك البعض.",
     "en": "That is: of that portion [of expressions]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: ذلك البعض.",
     "en": "That is: that portion."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "اعلم أنه لو قال المصنف: «وضع لمفرد» لكان التعريف أخصر وأسلم، إلا أنه أدرج المعنى لفائدة.",
     "en": "Know that had the author said “posited for a singular,” the definition would have been more concise and sounder; however, he inserted “meaning” for a benefit."},
    {"type": "pair",
     "ar": "فإن قلت: بعد تعريف المعنى بما يقصد بشيء، كيف يصح هذا السؤال؟",
     "en": "If you say: after “meaning” has been defined as “that which is intended by a thing,” how can this question [still] be valid?"},
    {"type": "pair",
     "ar": "قلت: لما تقرر عند السائل مقدمة وهمية، هي أن المعنى لا يكون لفظا لكثرة استعمال اللفظ في مقابلة المعنى، خص كلمة «ما» في تعريف المعنى بما سوى اللفظ. وتخصيص كلمة «ما» في التعريفات سنة مؤكدة.",
     "en": "I say: since there was established in the questioner['s mind] an imagined premise — namely, that meaning cannot be a wording, owing to the frequent use of “wording” in opposition to “meaning” — he restricted the word “mā” in the definition of meaning to what is other than the wording. And the restricting of the word “mā” in definitions is an emphasized practice (sunna muʾakkada)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فيه: أنه إن أراد بمفهوم المعنى مفهوم ما يتعلق به القصد بعينه فظاهر البطلان؛ لأن المعنى ما يقصد بشيء، وهو أخص مما يتعلق به القصد.",
     "en": "In it [there is a difficulty]: if he intends by the concept of “meaning” the concept of “that to which the intention attaches” precisely, then [the definition’s] falsity is evident; for “meaning” is “that which is intended by a thing,” and this is more specific than “that to which the intention attaches.”"},
    {"type": "pair",
     "ar": "وإن أراد صدق ما يتعلق به القصد على المعنى، فصدق الأعم على الأخص لا يلزم من كونه أعم من اللفظ كون المعنى أعم.",
     "en": "And if he intends [merely] the applicability of “that to which the intention attaches” to “meaning,” then, [this being] the applying of the more general to the more specific, from its being more general than “wording” it does not follow that “meaning” is more general."},
    {"type": "pair",
     "ar": "ألا ترى أن الحيوان صادق على الإنسان، ولا يلزم من كونه أعم من الفرس كون الإنسان أعم منه.",
     "en": "Do you not see that “animal” applies truly to “man,” yet from its being more general than “horse” it does not follow that “man” is more general than it?"},
    {"type": "pair",
     "ar": "ويمكن أن يقال: أراد الأول. واللام في القصد للعهد الخارجي، فيؤول إلى القصد بشيء. نعم لو قال: ما يقصد بشيء لكان أخصر وأوضح.",
     "en": "It may be said [in reply]: he intended the first [sense]; and the lām in “al-qaṣd” (the intention) is for external definite reference (al-ʿahd al-khārijī), so it comes down to “the intention by a thing.” Indeed, had he said “that which is intended by a thing,” it would have been more concise and clearer."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "حاصله: نقض لتعريف الكلمة بعدم صدقه على بعض الأفراد، وناشئ من قيد الإفراد الذي هو صفة المعنى على الراجح، لكن بمدخلية الجواب السابق، فلذا فرع عليه بـ«الفاء»، فلا يرد أنه لا وجه لإيراد هذا السؤال ههنا.",
     "en": "Its upshot: [this is] a refutation of the definition of the “word” (kalima) by [showing] its failure to hold true of some of the individual instances, and it arises from the restriction “singularity” (ifrād) — which is, on the preferred view, an attribute of the meaning — but through the involvement of the preceding answer; that is why he made it follow from it with the fāʾ [of consequence]. So it cannot be objected that there is no basis for raising this question here."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: لا يكون موضوعا لمفرد، بل هو موضوع لمركب، فلا يكون التعريف جامعا.",
     "en": "That is: it would not be posited for a singular, but rather posited for a compound, so the definition would not be all-comprehensive (jāmiʿ)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: إلا أن هذه الألفاظ.",
     "en": "That is: except that these expressions [are singular]."},
]
