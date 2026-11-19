# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 383 (printed ٣٨٢)."""

PAGE_NUMBER = 383
PRINTED_PAGE = "٣٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإنهم إذا قالوا لأحد: أخبر عن الاسم الفلاني في الجملة الفلانية بـ«الذي»» at the foot of PDF p. 382.
    {"type": "matn",
     "ar": "بعد بيانهم طريقة الإخبار به لا بد له من تذكير كثير من مسائل النحو وتدقيق النظر فيها حتى يعلم أن ذلك الإخبار في أي اسم يصح وفي أي اسم يمتنع،",
     "en": "… after they have explained the method of making a predication with it, he must recall many questions of grammar and examine them closely, so as to know for which noun such a predication is valid and for which it is barred."},
    {"type": "matn",
     "ar": "فأراد المصنف الإشارة إلى هذا الباب، فقال: (وإذا أخبرت) أي: إذا أردت أن تخبر عن جزء جملة",
     "en": "The author wished to point to this chapter, so he said: (When you make a predication), that is, when you wish to make a predication about a part of a sentence"},
    {"type": "matn",
     "ar": "(بـ«الذي») أي: باستعانة «الذي[[١]]، أو التي، أو الألف واللام»، فإن الباء ليست صلة للإخبار؛ لأن «الذي» مخبر عنها[[٢]] لا مخبر بها",
     "en": "(with “alladhī”), that is, with the help of “alladhī, or allatī, or alif-lām”; for the bāʾ is not the complement of “predication”, since “alladhī” is predicated about, not predicated;"},
    {"type": "matn",
     "ar": "(صدرتها[[٣]]) أي: أوقعت كلمة «الذي»[[٤]] أو ما يقوم مقامها في صدر الجملة الثانية",
     "en": "(you put it at the head), that is, you place the word “alladhī”, or what stands in its place, at the head of the second sentence,"},
    {"type": "matn",
     "ar": "(وجعلت[[٥]] موضع المخبر عنه) أي: في موضع ما هو مخبر عنه بالذي[[٦]] في الجملة الثانية، يعني: في موضعه الذي كان له في الجملة الأولى",
     "en": "(and you put in the place of what is predicated about), that is, in the place of what is predicated about with alladhī in the second sentence, he means in the place it had in the first sentence,"},
    {"type": "matn",
     "ar": "(ضميرا لها) أي: لكلمة الذي (وأخرته[[٧]] عنه) أي: المخبر عنه عن الضمير[[٨]] (خبرا) نصب على الحال، أو ضمن «أخرته» معنى جعلته، أعني: جعلته، خبرا متأخرا.",
     "en": "(a pronoun for it), that is, for the word alladhī, (and you put it after it), that is, you put what is predicated about after the pronoun, (as a predicate): accusative as a circumstantial qualifier (ḥāl); or “akhkhartahu” is made to include the meaning of “jaʿaltahu”, that is, you made it a predicate placed later."},
    {"type": "matn",
     "ar": "(فإذا أخبرت) مثلا (عن «زيد» من) جملة («ضربت زيدا») بكلمة الذي أوقعتها في صدر الجملة الثانية،",
     "en": "(So when you make a predication), for example, (about “Zayd” in) the sentence (“ḍarabtu Zaydan”) (I struck Zayd) with the word alladhī, you place it at the head of the second sentence,"},
    {"type": "matn",
     "ar": "وجعلت في موضع ما هو مخبر عنه في هذه الجملة، أعني: «زيدا»، والمراد بموضعه محله الذي كان له في الجملة الأولى،",
     "en": "and you put in the place of what is predicated about in this sentence, namely “Zaydan”—by its place is meant the position it had in the first sentence—"},
    # REVIEW: «وهو محل في المفعول» printed clearly (one might expect «وهو محل المفعول»); transcribed as printed.
    {"type": "matn",
     "ar": "وهو محل في المفعول من «ضربت» ضمير للذي، وأخرت المخبر عنه يعني: زيدا وجعلته خبرا عن «الذي»،",
     "en": "which is the position of the object of “ḍarabtu”, a pronoun for alladhī; and you put what is predicated about, namely Zayd, at the end and made it the predicate of “alladhī”,"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: بما يعبر عنه بالذي، فالباء صلة الإخبار.",
     "en": "That is, by means of what is expressed by alladhī; so the bāʾ is the complement of “predication”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: بحسب الذكر. وأما ذات المخبر عنه فهو «زيد» في المثال المذكور. ولذا قال: فإذا أخبرت عن زيد إلى آخره.",
     "en": "That is, with respect to mention. As for the actual thing predicated about, it is “Zayd” in the example given; hence he said “so when you make a predication about Zayd …”."},
    {"type": "pair",
     "ar": "وإنما اعتبر هذا الوصف بالقياس إلى زيد دون الذي مع أنه المخبر عنه بحسب الظاهر؛ لأن شأن المخبر عنه أن يكون مفروغا عنه.",
     "en": "He took this description in relation to Zayd rather than alladhī, although that is what is apparently predicated about, because what is predicated about should be something settled."},
    # REVIEW: «مفروغا» printed in the accusative where a nominative predicate is expected; transcribed as printed.
    {"type": "pair",
     "ar": "والجملة الأولى مع أجزائها مفروغا عنها دون الموصول.",
     "en": "The first sentence with its parts is settled, not the relative noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا يشعر بأن يكون من مواضع وجوب تقديم المبتدأ أن يكون موصولا، ولم يذكر في موضع في شيء من كتب النحو،",
     "en": "This suggests that among the cases where the subject must be put first is its being a relative noun, yet this is not mentioned anywhere in any book of grammar."},
    {"type": "pair",
     "ar": "فلعلهم أرادوا التصدير عملا بما هو الأصل في باب المبتدأ.",
     "en": "Perhaps they intended putting it at the head in keeping with what is the norm in the chapter on the subject."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن المطلوب أن يخبر عن الموصول، والمخبر عنه في الاسمية مبتدأ، والمبتدأ مرتبته الصدر.",
     "en": "Because the aim is to predicate about the relative noun, and what is predicated about in a nominal sentence is the subject, whose rank is the head."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن المطلوب أن تصف الموصول بالوصف بالذي كان لذلك المخبر عنه بلا تغيير شيء من الجملة الأولى،",
     "en": "Because the aim is to describe the relative noun by the description that belonged to that thing predicated about, without changing anything in the first sentence;"},
    # REVIEW: printed «ولم يكن أن يكون» (the sense calls for «ولم يمكن»); transcribed as printed.
    {"type": "pair",
     "ar": "ولم يكن أن يكون الموصول مكان المخبر عنه لتصديره مبتدأ، فلا بد أن يكون نائبه وهو الضمير العائد إليه مكانه.",
     "en": "and the relative noun could not be in the place of what is predicated about, since it is put at the head as subject; so its substitute, the pronoun returning to it, must be in its place."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يريد أن التعبير بالمخبر عنه باعتبار ما يؤول.",
     "en": "He means that the expression “what is predicated about” is used with regard to what it will become."},
    {"type": "pair",
     "ar": "ولك أن تريد بكلمة «عن» التعليل أي: المخبر عن جهته وبسببه.",
     "en": "You may also take the word “ʿan” as causal, that is, what is predicated on its account and because of it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأنه خبر، وحق الخبر التأخير.",
     "en": "Because it is a predicate, and the predicate’s due place is after."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "اعتبر التأخير بالنسبة إلى الضمير، والظاهر اعتباره مقابلا للتصدير، فيكون بالنسبة إلى الجملة.",
     "en": "He took the placing-after in relation to the pronoun; the evident course is to take it as the counterpart of putting at the head, so that it is in relation to the sentence."},
]
