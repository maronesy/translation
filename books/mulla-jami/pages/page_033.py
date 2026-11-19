# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 33 (printed ٣٢)."""

PAGE_NUMBER = 33          # PDF page
PRINTED_PAGE = "٣٢"       # page number printed in the book

BLOCKS = [
    # ---------------- The main commentary text (matn) ----------------
    # (continues "…لجواز اتصاف" from the previous page)
    {"type": "matn",
     "ar": "الجنس بالوحدة[[١]]، والواحد بالجنسية[[٢]].",
     "en": "…[for] the genus to be qualified by unity, and the unit by genericness."},
    {"type": "matn",
     "ar": "يقال: «هذا الجنس واحد»، و«ذلك الواحد جنس».",
     "en": "One says: “this genus is one,” and “that one is a genus.”"},
    {"type": "matn",
     "ar": "ويمكن حملها[[٣]] على العهد الخارجي بإرادة الكلمة المذكورة على ألسنة النحاة.",
     "en": "It is possible to construe it [the lām] as denoting external, definite reference (al-ʿahd al-khārijī), by intending the word (kalima) as it is current on the tongues of the grammarians."},
    {"type": "matn",
     "ar": "«لفظ»: اللفظ في اللغة: الرمي[[٤]]، يقال: «أكلت التمرة، ولفظت النواة»، أي: رميتها[[٥]]،",
     "en": "“Lafẓ” (an utterance): al-lafẓ in the language means “throwing” (al-ramy); one says, “I ate the date and I cast out (lafaẓtu) the pit,” meaning: I threw it."},
    {"type": "matn",
     "ar": "ثم نقل في عرف النحاة[[٦]] ابتداء[[٧]]، أو بعد جعله[[٨]] بمعنى الملفوظ[[٩]]، كـ«الخلق» بمعنى المخلوق، إلى ما يتلفظ به الإنسان[[١٠]] حقيقة كان أو حكما، مهملا",
     "en": "Then it was transferred, in the usage of the grammarians — either from the outset (ibtidāʾan), or after [first] making it [mean] “the uttered” (al-malfūẓ), like “al-khalq” (creation) used to mean al-makhlūq (the created thing) — to that which a human being pronounces, whether in reality or in ruling (ḥukman), be it meaningless (muhmal)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "طبيعية كانت أو صناعية أو غير ذلك. وفيه نظر؛ لأن هذه الوحدة مغايرة للوحدة التي هي مدلول التاء، فإنها فردية لا جنسية.",
     "en": "Whether [the unity be] natural, conventional, or otherwise. But there is [room for] reflection in this, because this unity is different from the unity that is the signification of the tāʾ, for the latter is individual, not generic."},
    {"type": "pair",
     "ar": "ويمكن أن يجاب: بأن الكلمة اللغوية إذا خصت بما هو مصطلح النحاة صارت الوحدة التي هي في الكلمة اللغوية وحدة جنسية.",
     "en": "One may answer: that when the linguistic “kalima” is specified to what is the technical term of the grammarians, the unity that is in the linguistic kalima becomes a generic unity."},
    {"type": "pair",
     "ar": "ويلزم من ذلك ألا تكون نسبة الكلمة الاصطلاحية إلى الكلمة اللغوية نسبة «تمرة» إلى «تمر».",
     "en": "And it follows from this that the relation of the technical kalima to the linguistic kalima is not [like] the relation of “tamra” to “tamr.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن بين الجنس والواحد تصادقا، فيجوز أن يجعل الجنس أصلا، والواحد وصفا له، وأن ينعكس.",
     "en": "He means: that between the genus and the unit there is mutual applicability (taṣāduq); so it is permissible to make the genus the base (aṣl) and the unit a description of it, and [also] the reverse."},

    {"type": "pair",
     "ar": "فاعلم أن الوحدة نوعان: جنسية وفردية، أي: إما صفة للجنس أو صفة لفرد من الجنس؛",
     "en": "Know that unity is of two kinds: generic (jinsiyya) and individual (fardiyya) — that is, either a description of the genus or a description of an individual of the genus."},
    {"type": "pair",
     "ar": "يقال: هذا جنس واحد، وهذا واحد من الجنس، فاتصف الجنس بالواحد، وبالعكس، فلا منافاة بينهما، بل هما يتصادقان.",
     "en": "One says: “this is one genus,” and “this is one [individual] of the genus.” So the genus is qualified by the unit, and vice versa; hence there is no contradiction between the two — rather, they are mutually applicable."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: اللام.",
     "en": "That is: the lām."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ورمي الشيء من الفم والتكلم.",
     "en": "And the throwing of a thing from the mouth, and speaking."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: النواة.",
     "en": "That is: the pit."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا الاصطلاح غير مختص بالنحاة، بل جميع أرباب العربية يريدون هذا المعنى.",
     "en": "This technical usage is not specific to the grammarians; rather all masters of the Arabic [sciences] intend this meaning."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "منصوب على الظرفية.",
     "en": "[It is] accusative as an adverbial of place/time (ẓarfiyya)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: جعل اللفظ.",
     "en": "That is: the making of the utterance [into a name]."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فعلى الأول: لا يحتاج إلى مؤنة تعدد النقل، وهو من قبيل تسمية المسبب باسم السبب، أو تسمية المتعلق -بالفتح- باسم المتعلق -بالكسر.",
     "en": "On the first [reading]: there is no need for the burden of multiple transferals; and it is of the category of naming the effect by the name of the cause, or naming the object of relation (al-mutaʿallaq — with a fatḥa) by the name of that which relates (al-mutaʿalliq — with a kasra)."},
    {"type": "pair",
     "ar": "وعلى الثاني: يكون العلاقة بين المنقول إليه والمنقول عنه أقوى؛ إذ يكون الملفوظ بمعنى المرمي حقيقة، والمعنى المنقول إليه هو ما يتلفظ به حقيقة وحكما،",
     "en": "On the second [reading]: the relation between that to which [the term] is transferred and that from which it is transferred is stronger; for “the uttered” (al-malfūẓ) would be [used] in the meaning of “the thrown” (al-marmī) in reality, while the meaning to which it is transferred is that which is pronounced in reality and in ruling."},
    {"type": "pair",
     "ar": "فيكون النسبة بين المعنى المنقول عنه والمنقول إليه هي العموم من وجه، فلم يكن من قبيل تسمية الخاص باسم العام.",
     "en": "So the relation between the meaning transferred-from and the meaning transferred-to is [one of] partial overlap (al-ʿumūm min wajh); hence it is not of the category of naming the specific by the name of the general."},
    {"type": "pair",
     "ar": "قال الفاضل المحشي: ويجوز أن يجعل اللفظ منقولا من الرمي بمعنى اللفظ من الفم، أو بمعنى التكلم، ابتداء، أو بواسطة.",
     "en": "The learned glossator (al-fāḍil al-muḥashshī) said: it is [also] permissible to make al-lafẓ transferred from al-ramy in the sense of “the utterance from the mouth,” or in the sense of “speaking” — either from the outset (ibtidāʾan) or by means of an intermediary (bi-wāsiṭa)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "الباء للتعدية، والتلفظ بمعنى التكلم والنطق.",
     "en": "The bāʾ is for transitivity (taʿdiya), and al-talaffuẓ is in the meaning of speaking (al-takallum) and articulation (al-nuṭq)."},
]
