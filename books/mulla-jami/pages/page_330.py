# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 330 (printed ٣٢٩)."""

PAGE_NUMBER = 330
PRINTED_PAGE = "٣٢٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # New sentence: follows «وبعضهم إلى أنه عطف بيان.» at the foot of PDF p. 329.
    {"type": "matn",
     "ar": "(و) مثل: «مررت (بزيد هذا»[[١]]) أي: بـ«زيد» المشار إليه بـ«هذا»،",
     "en": "(And) as in “I passed (by Zayd, this one)” (marartu bi-zaydin hādhā), that is, by Zayd who is pointed to by “hādhā.”"},
    {"type": "matn",
     "ar": "فـ«هذا» في هذا الموضع يدل على معنى حاصل في ذات زيد، فوقع صفة له،",
     "en": "So “hādhā” in this place signifies a meaning present in the essence of Zayd, and it therefore occurred as an adjective of it;"},
    {"type": "matn",
     "ar": "وفي المواضع الأخر التي لا تدل[[٢]] على هذا المعنى[[٣]] لا يصح أن يقع صفة.",
     "en": "while in the other places, which do not signify this meaning, it cannot soundly occur as an adjective."},
    {"type": "matn",
     "ar": "(وتوصف النكرة) لا المعرفة[[٤]] (بالجملة الخبرية) التي هي في حكم النكرة[[٥]]؛",
     "en": "(The indefinite noun (nakira) is qualified)—not the definite (maʿrifa)—(by the declarative sentence (al-jumla al-khabariyya)), which has the status of an indefinite;"},
    {"type": "matn",
     "ar": "لأن الدلالة على معنى[[٦]] في متبوعه، كما توجد في المفرد كذلك توجد في الجملة الخبرية،",
     "en": "for signification of a meaning in its qualified word, just as it is found in the single word (mufrad), is likewise found in the declarative sentence."},
    {"type": "matn",
     "ar": "وإنما قيد الجملة بالخبرية؛ لأن الإنشائية لا تقع صفة[[٧]] إلا بتأويل بعيد[[٨]]،",
     "en": "He restricted the sentence to the declarative only because the non-declarative (inshāʾiyya) does not occur as an adjective except by a far-fetched interpretation,"},
    {"type": "matn",
     "ar": "كما إذا قلت: «جاءني رجل اضربه» أي: مقول في حقه اضربه، أي: مستحق لأن يؤمر بضربه.",
     "en": "as when you say “A man came to me—strike him!” (jāʾanī rajulun iḍribhu), that is, one of whom it is said “strike him,” that is, deserving that one be ordered to strike him."},
    {"type": "matn",
     "ar": "(ويلزم) فيها (الضمير) الراجع إلى تلك النكرة للربط، نحو: «جاءني رجل أبوه قائم»،",
     "en": "(And there must be) in it (a pronoun) referring back to that indefinite noun, for linkage (rabṭ), as in “A man came to me whose father is standing.”"},
    {"type": "matn",
     "ar": "وإذا لم يكن فيها الضمير الرابط تكون أجنبية[[٩]] بالنسبة إلى الموصوف، فلا",
     "en": "If there is no linking pronoun in it, it is extraneous (ajnabiyya) in relation to the qualified noun, so it does not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: اسم الإشارة يقع وصفا للعلم، والمضاف إلى المضمر وإلى العلم وإلى اسم الإشارة؛ لأن الموصوف أخص أو مساو.",
     "en": "Shaykh al-Raḍī said: The demonstrative noun occurs as a description of the proper name (ʿalam) and of what is annexed to a pronoun, to a proper name or to a demonstrative noun, because the qualified noun is more specific or equal [in specificity]."},
    {"type": "pair",
     "ar": "وأما في غير هذه المواضع، فلا يقع صفة.",
     "en": "In places other than these, it does not occur as an adjective."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا يقصد بدلالته هذا المعنى.",
     "en": "That is, this meaning is not intended by its signification."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: دلالة مقصودة.",
     "en": "That is, an intended signification."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إلا معرف باللام لا يشير بها إلى واحد بعينه؛ لأن تعريفه لفظي.",
     "en": "Except a noun made definite by the lām by which no particular individual is pointed to, since its definiteness is merely verbal (lafẓī)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لعدم الإشارة إلى معلومية مضمونها، لكنها ليست نكرة؛ لأنها والمعرفة من أقسام الذات والاسم.",
     "en": "Because there is no indication that its content is known; yet it is not an indefinite, since the indefinite and the definite are divisions of the essence and of the noun."},
    {"type": "pair",
     "ar": "وفي قوله: «في حكم النكرة» إشارة إلى توجيه قولهم: إن النعت يوافق المنعوت تعريفا وتنكيرا مع أن الجملة قد تكون نعتا وليس معرفة ولا نكرة.",
     "en": "In his words “has the status of an indefinite” there is an indication of how to account for their statement that the qualifier agrees with the qualified in definiteness and indefiniteness, although the sentence is sometimes a qualifier while being neither definite nor indefinite."},
    {"type": "pair",
     "ar": "ويمكن تخصيص الحكم بالنعت المفرد، أو توجيهه بأن الجملة في تأويل النكرة كما قاله الشيخ الرضي من أن قام رجل ذهب أبوه في تأويل ذاهب أبوه، وأبوه زيد في تأويل كائن أبوه زيد.",
     "en": "The rule may be restricted to the single-word qualifier, or accounted for by the sentence being interpreted as an indefinite, as Shaykh al-Raḍī said: “A man whose father went stood up” is to be interpreted as “whose father is going,” and “whose father is Zayd” as “whose father is being Zayd.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قد سوى الشيخ الرضي بين النعت المفرد والجملة، والمشهور أن المفرد أصل،",
     "en": "Shaykh al-Raḍī placed the single-word qualifier and the sentence on a par, while the well-known view is that the single word is the base (aṣl);"},
    {"type": "pair",
     "ar": "لعل وجهه أن الجملة التي لها محل من الإعراب إنما تكون في تأويل المفرد.",
     "en": "perhaps the reason is that a sentence that has a place in inflection (maḥall min al-iʿrāb) is only ever interpreted as a single word."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن الصفة يجب أن يكون مضمونها معلوما للمخاطب قبل ذكرها حتى يصح فائدتها،",
     "en": "Because the content of an adjective must be known to the addressee before it is mentioned, so that its benefit may be sound,"},
    {"type": "pair",
     "ar": "وهي أن يعرف المخاطب الموصوف المبهم بما يكون معلوما له، والإنشائية لا يكون مضمونها معلوما للمخاطب قبل ذكرها، وكذا حكم الصلة.",
     "en": "namely that the addressee should come to know the indeterminate qualified noun through something known to him; and the content of a non-declarative sentence is not known to the addressee before it is mentioned. The same is the rule for the relative clause (ṣila)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ذلك في الطلبية المحكية بقول محذوف كقوله: جاؤوا بمذق هل رأيت الذئب قط أي: بمذق مقول عنده هذا القول كما يكون في الحال،",
     "en": "That is in the case of a request sentence (ṭalabiyya) reported by an elided verb of saying, as in the poet’s words “They brought diluted milk—have you ever seen the wolf?”, that is, diluted milk at which this saying is said; as also occurs in the circumstantial qualifier (ḥāl),"},
    {"type": "pair",
     "ar": "والمفعول الثاني من باب «علمت» مثل أبي الدرداء رضي الله عنه: وجدت الناس اخبر تقله.",
     "en": "and in the second object of the class of “ʿalimtu” (I knew), as in [the saying of] Abū l-Dardāʾ, may Allah be pleased with him: “I found people [such that one says]: test [them] and you will detest [them]” (wajadtu l-nāsa ukhbur taqlih)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    # REVIEW: «للمتعلقه» (lām + article + pronoun) is printed thus; one would expect «لمتعلقه»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: لم يكن حالا لنفس الموصوف ولا للمتعلقه.",
     "en": "That is, it would not be a state of the qualified itself nor of what is connected with it."},
    {"type": "pair",
     "ar": "وفي الملازمة مناقشة لجواز حصول الربط بغير الضمير، كما في خبر المبتدأ.",
     "en": "There is room for dispute about the entailment, since linkage may be achieved without a pronoun, as in the predicate of the subject (khabar al-mubtadaʾ)."},
]
