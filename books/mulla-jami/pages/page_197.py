# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 197 (printed ١٩٦)."""

PAGE_NUMBER = 197
PRINTED_PAGE = "١٩٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وإما وجوبا فيما تضمن[[١]] معنى استفهام أو شرط نحو: «من رأيت؟ ومن تكرم يكرمك».",
     "en": "Or obligatorily, in what contains the sense of an interrogative or a condition, as in: “Whom did you see?” (man raʾayta) and “Whomever you honour will honour you” (man tukrim yukrimka)."},
    {"type": "matn",
     "ar": "وهذا إذا لم يكن مانع من التقدم، كوقوعه في حيز «أن»[[٢]] نحو: «من البر أن تكف لسانك».",
     "en": "This is when there is no impediment to its preceding, such as its falling within the scope of “an,” as in: “It is part of piety that you restrain your tongue” (mina al-birri an takuffa lisānaka)."},
    {"type": "matn",
     "ar": "(وقد يحذف الفعل) العامل في المفعول به (لقيام قرينة[[٣]]) مقالية أو حالية",
     "en": "(And the verb) governing the direct object (may be elided when there is an indication—qarīna), verbal or circumstantial,"},
    {"type": "matn",
     "ar": "(جوازا نحو: زيدا لمن قال من أضرب؟) أي: «أضرب زيدا»، فحذف الفعل للقرينة المقالية التي هي السؤال،",
     "en": "(optionally, as in “Zaydan,” [said] to one who asked “Whom shall I strike?”), that is: “Strike Zayd”; the verb was elided because of the verbal indication, namely the question;"},
    {"type": "matn",
     "ar": "ونحو: «مكة» للمتوجه إليها، أي: «تريد مكة؟»[[٤]]، فحذف الفعل للقرينة الحالية.",
     "en": "and as in “Makkata” [said] to one heading towards it, that is: “You want Mecca?”; the verb was elided because of the circumstantial indication."},
    {"type": "matn",
     "ar": "(ووجوبا في أربعة مواضع) تخصيصها بالذكر ليس للحصر[[٥]]، لوجوب الحذف في باب الإغراء[[٦]]، والمنصوب على المدح أو الذم أو الترحم",
     "en": "(And obligatorily in four places.) Singling them out for mention is not for restriction, since elision is obligatory in the chapter of incitement (ighrāʾ) and in the accusative of praise, blame or pity,"},
    {"type": "matn",
     "ar": "نحو: «أخاك أخاك» أي: الزمه، بل لكثرة مباحثها بالنسبة إلى هذه الأبواب.",
     "en": "as in “Your brother, your brother!” (akhāka akhāka), that is: keep to him; rather, it is because their topics are more numerous in comparison with these chapters."},
    {"type": "matn",
     "ar": "(الأول) من تلك المواضع الأربعة (سماعي) أي: مقصور على السماع لا يتجاوز عن أمثلة محدودة مسموعة بأن يقاس عليها أمثلة أخرى",
     "en": "(The first) of those four places (is heard usage—samāʿī), that is: restricted to what is heard [from the Arabs]; it does not go beyond a limited number of attested examples so that other examples might be formed on their analogy,"},
    {"type": "matn",
     "ar": "(نحو: «امرأ ونفسه»[[٧]]) أي: اترك أمرا أو نفسه",
     "en": "(as in: “imraʾan wa-nafsahu”—a man and himself), that is: leave a man [alone], or himself;"},
    {"type": "matn",
     "ar": "(﴿انتهوا خيرا لكم﴾[[٨]])[[٩]] أي: انتهوا عن التثليث واقصدوا خيرا",
     "en": "(“Desist—[it is] better for you”), that is: desist from [the doctrine of] the Trinity and aim at something better…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وكذا فيما إذا كان معمولا لما يلي الفاء التي في جواب «أما». ولم يكن له منصوب سواه",
     "en": "Likewise where it is governed by what follows the fāʾ in the apodosis of “ammā,” and [that governor] has no other accusative,"},
    {"type": "quran",
     "ar": "كقوله تعالى: ﴿فأما اليتيم فلا تقهر﴾ (سورة الضحى: ٩).",
     "en": "as in His words, the Exalted: “As for the orphan, do not oppress [him]” (Qurʾān, Sūrat al-Ḍuḥā 93:9)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وكوقوع فعله مؤكدا بالنون؛ لأن تقديمه دليل في ظاهر الأمر على أن الفعل غير مهم،",
     "en": "And such as its verb’s being emphasized with the nūn [of emphasis]; because putting [the object] first is, on the face of it, a sign that the verb is not of concern,"},
    {"type": "pair",
     "ar": "وتوكيد الفعل مؤذن بكونه مهما، فيتنافران في الظاهر.",
     "en": "while emphasizing the verb announces that it is of concern; so the two are outwardly incompatible."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اللام للتوقيت. أي: وقت قيام قرينة لا للتعليل، فإن التعليل لقيام القرينة إنما يصح في الحذف جوازا.",
     "en": "The lām is temporal, that is: “at the time an indication is present,” not causal; for making the presence of the indication the cause holds only for optional elision."},
    {"type": "pair",
     "ar": "وأما في الحذف وجوبا فلا يكفي القرينة، بل لا بد مع القرينة من أمر آخر ليحذف،",
     "en": "In obligatory elision the indication does not suffice; rather something else besides the indication is required for it to be elided."},
    {"type": "pair",
     "ar": "فلم يكن قيام القرينة علة الحذف، بل في وقت قيامها تحقق باعث الحذف.",
     "en": "So the presence of the indication is not the cause of elision; rather, at the time of its presence the motive for elision is realized."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأولى أي: أتريد مكة؟ بالاستفهام.",
     "en": "Better would be “that is: a-turīdu Makkata? (Do you want Mecca?)” with the interrogative [particle]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ذكر الجمهور على أن العدد لا يفيد الحصر. فإن قلت: فما فائدة ذكره؟",
     "en": "The majority have stated that a number does not convey restriction. If you say: then what is the benefit of mentioning it?"},
    # REVIEW: print clearly reads «ولا ينقلب شيء»; the sense suggests «ولا ينفلت شيء» (nothing escapes); transcribed as printed.
    {"type": "pair",
     "ar": "قلت: لينضبط المذكور عند السامع، ولا ينقلب شيء،",
     "en": "I say: so that what is mentioned is held firmly by the hearer, and nothing is turned about (lā yanqalibu shayʾ);"},
    {"type": "pair",
     "ar": "لكن يتجه أن المذكور خمسة، خامسها: المندوب على طريقة المصنف. فرعاية مذهبه تقتضي أن يجعل الأبواب خمسة.",
     "en": "but the objection arises that what is mentioned is five, the fifth being the lamented noun (al-mandūb) according to the author’s method; so regard for his position requires that the chapters be made five."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أشار في الحاشية إلى تعريف الأمور الأربعة بأمثلتها حيث قال: نحو: «أخاك أخاك» أي: الزمه،",
     "en": "In the marginal gloss he indicated the definition of the four matters by their examples, where he said: as in “akhāka akhāka,” that is: keep to him;"},
    {"type": "pair",
     "ar": "ونحو: «الحمد لله الحميد»، ونحو: «أتاني زيد الفاسق الخبيث»، ونحو: «مررت بزيد المسكين».",
     "en": "and as in “Praise be to Allah, the Praiseworthy” (al-ḥamdu li-llāhi al-ḥamīda); and as in “Zayd came to me, the wicked, the vile”; and as in “I passed by Zayd, the poor man.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الواو إما للعطف، ومعناه: الحث على الفرار عن نفسه، وإما بمعنى «مع» ومعناه: قصر يده ولسانه عنه.",
     "en": "The wāw is either for coordination, its sense being an urging to flee from [the man] himself; or it is in the sense of “with” (maʿa), its sense being: restrain his hand and tongue from him."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة النساء: ١٧١.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:171."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: مما أنتم فيه.",
     "en": "That is: than that in which you are."},
    {"type": "pair",
     "ar": "والقرينة على تقدير الفعل أنك إذا نهيت عن شيء، ثم جيء بما لا ينهى عنه، بل هو مما يؤمر به انساق الذهن إلى نحو: اقصد أو ائت، أو ما يفيد هذا المعنى،",
     "en": "The indication for supposing the verb is that, when you forbid something and then there comes what is not forbidden but is among what is commanded, the mind is led to the like of “aim at” or “come to,” or what conveys this sense;"},
    {"type": "pair",
     "ar": "وليست هذه ضابطة لوجوب",
     "en": "and this is not a rule for the obligatoriness…"},
]
