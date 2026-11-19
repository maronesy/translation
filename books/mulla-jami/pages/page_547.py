# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 547 (printed ٥٤٦)."""

PAGE_NUMBER = 547
PRINTED_PAGE = "٥٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأنها للتقليل» at the foot of PDF p. 546 (mid-sentence).
    {"type": "matn",
     "ar": "المحقق، ولا يتصور ذلك إلا في الماضي، نحو: «رب رجل كريم لقيته»، أو «رب رجل كريم لم أفارقه».",
     "en": "…of what is actual, and that is conceivable only in the past, as in “many a generous man have I met” or “many a generous man have I not parted from”."},
    {"type": "matn",
     "ar": "(محذوف) أي: ذلك الفعل الماضي.",
     "en": "(Elided), that is, that past verb [is elided]"},
    {"type": "matn",
     "ar": "(غالبا) أي: في غالب الاستعمالات، لوجود القرائن نحو: «رب رجل كريم» أي: لقيته.",
     "en": "(mostly), that is, in most usages, because contextual indicators are present, as in “rubba rajulin karīmin” (many a generous man), that is, I have met."},
    {"type": "matn",
     "ar": "(وقد تدخل) أي: «رب» (على مضمر مبهم) لا مرجع له[[١]] (مميز بنكرة منصوبة) على التمييز",
     "en": "(And it sometimes enters), that is, “rubba”, (upon a vague pronoun) that has no antecedent, (specified by an indefinite noun in the accusative) as a specification (tamyīz);"},
    {"type": "matn",
     "ar": "(والضمير مفرد) وإن كان المميز مثنى أو مجموعا (مذكر[[٢]]) وإن كان المميز مؤنثا،",
     "en": "(and the pronoun is singular), even if the specification is dual or plural, (and masculine), even if the specification is feminine,"},
    {"type": "matn",
     "ar": "نحو: «ربه رجلا، أو رجلين، أو رجالا، أو امرأة، أو امرأتين، أو نساء».",
     "en": "as in “rubbahu rajulan” (many a man), or “rajulayn”, or “rijālan”, or “imraʾatan”, or “imraʾatayn”, or “nisāʾan”."},
    {"type": "matn",
     "ar": "(خلافا للكوفيين في مطابقة التمييز) في الإفراد والتثنية والجمع، والتذكير والتأنيث،",
     "en": "(Contrary to the Kūfans regarding agreement with the specification) in singular, dual and plural, and in masculine and feminine;"},
    {"type": "matn",
     "ar": "فإنهم يقولون: «ربه رجلا، وربهما رجلين، وربهم رجالا، وربها امرأة، وربهما امرأتين، وربهن نساء».",
     "en": "for they say “rubbahu rajulan”, “rubbahumā rajulayn”, “rubbahum rijālan”, “rubbahā imraʾatan”, “rubbahumā imraʾatayn” and “rubbahunna nisāʾan”."},
    {"type": "matn",
     "ar": "(وتلحقها) أي: «رب» («ما» الكافة) أي: المانعة عن العمل (فتدخل) بعد لحوق «ما» (على الجمل) نحو: ﴿ربما يود الذين كفروا﴾[[٣]].",
     "en": "(And there attaches to it), that is, to “rubba”, (the restraining (kāffa) “mā”), that is, the one that prevents [it from] governing, (so it enters), after “mā” has attached, (upon sentences), as in “Perhaps (rubamā) those who disbelieve will wish”."},
    {"type": "matn",
     "ar": "وقد تكون «ما» زائدة، فتدخل على الاسم، وتجره نحو:",
     "en": "Sometimes “mā” is redundant, so it enters upon a noun and puts it in the genitive, as in:"},
    {"type": "verse",
     "ar": "ربما ضربة بسيف صقيل          بين بصرى وطعنة نجلاء",
     "en": "Many a blow with a burnished sword between [here and] Buṣrā, and many a wide-gaping thrust."},
    {"type": "matn",
     "ar": "(وواوها) أي: واو «رب» في حكمها[[٤]].",
     "en": "(And its wāw), that is, the wāw of “rubba”, is in its status."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عند البصريين؛ إذ لو كان له مرجع لما احتاج إلى التمييز خلافا للكوفيين،",
     "en": "According to the Baṣrans; for if it had an antecedent it would not need a specification. This is contrary to the Kūfans,"},
    {"type": "pair",
     "ar": "فإنهم قالوا: إن الضمير راجع إلى مذكور كأن قائلا قال: هل من رجل كريم، فقيل له: ربه رجلا،",
     "en": "for they said that the pronoun refers to something mentioned, as though someone had said “is there any generous man?” and was told “rubbahu rajulan”;"},
    {"type": "pair",
     "ar": "وإنما احتاج إلى التمييز لعدم كون المرجع مذكورا في هذا الكلام.",
     "en": "it needs a specification only because the antecedent is not mentioned in this sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه أشد إبهاما من غيره، والقصد بهذا الضمير الإبهام، فما كان أشد كان أنسب مع أمن اللبس بالتمييز.",
     "en": "Because it is vaguer than the others, and what is intended by this pronoun is vagueness; so what is vaguer is more fitting, ambiguity being prevented by the specification."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الحجر: ٢.",
     "en": "Qurʾān, Sūrat al-Ḥijr 15:2."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كأنه أشار إلى أن الأولى أن: يقول واوها في حكمها، ولا يخص مشاركتهما بالدخول على نكرة موصوفة.",
     "en": "It is as though he indicated that it is better to say “its wāw is in its status” and not to restrict their sharing to entering upon a qualified indefinite noun."},
    # REVIEW: «وكان المصنف» is printed; the sense seems to require «وكأن المصنف» ("it is as though the author"). Transcribed as printed.
    {"type": "pair",
     "ar": "وكان المصنف لم يقل: واوها في حكمها، لئلا يفيد لحوق ما الكافة بالواو، ودخولها على الضمير.",
     "en": "[It is as though] the author did not say “its wāw is in its status”, lest it imply that the restraining “mā” attaches to the wāw and that it enters upon the pronoun."},
    {"type": "pair",
     "ar": "وقال: وتدخل على نكرة موصوفة تنبيها على أن التفاوت بينهما في مجرد اختصاص الواو بالنكرة الموصوفة دون الضمير، ودون الجمل لعدم لحوق ما الكافة بالواو، فلا يصح دخولها على الجمل.",
     "en": "Instead he said “and it enters upon a qualified indefinite noun”, to point out that the difference between the two lies only in the wāw’s being restricted to the qualified indefinite noun, not the pronoun, and not sentences, since the restraining “mā” does not attach to the wāw; so its entry upon sentences is not valid."},
]
