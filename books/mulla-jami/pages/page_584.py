# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 584 (printed ٥٨٣)."""

PAGE_NUMBER = 584
PRINTED_PAGE = "٥٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[حرفا الاستفهام]",
     "en": "The Two Particles of Interrogation (ḥarfā al-istifhām)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "حرفا الاستفهام: «الهمزة»، و«هل». لهما صدر الكلام، وتدخلان على الاسمية والفعلية.",
     "en": "The two particles of interrogation: “hamza” and “hal”. They take the head of the sentence, and they enter upon the nominal and the verbal [sentence]."},
    # Punctuation «و)،» printed as such.
    {"type": "matn",
     "ar": "(تقول) في الاسمية («أزيد قائم؟» و)، في الفعلية («أقام زيد؟» وكذلك «هل»)",
     "en": "(You say), in the nominal, (“a-Zaydun qāʾimun?” [is Zayd standing?], and), in the verbal, (“a-qāma Zaydun?” [did Zayd stand?]; and likewise “hal”):"},
    {"type": "matn",
     "ar": "تقول فيهما: «هل زيد قائم؟ وهل قام زيد؟»، إلا أن الهمزة تدخل على كل اسمية، سواء كان الخبر فيها اسما أو فعلا،",
     "en": "you say in both: “hal Zaydun qāʾimun? wa-hal qāma Zaydun?”. However, the hamza enters upon every nominal [sentence], whether its predicate is a noun or a verb,"},
    {"type": "matn",
     "ar": "بخلاف «هل»، فإنها لا تدخل على اسمية خبرها فعل، نحو: «هل زيد قام؟» إلا على شذوذ،",
     "en": "unlike “hal”, for it does not enter upon a nominal [sentence] whose predicate is a verb, as in “hal Zaydun qāma?”, except anomalously;"},
    # REVIEW: the Qurʾānic «الإنسان» is printed in the Qurʾān font as alif with hamza above
    # and a kasra below; written here as «الإنسان».
    {"type": "matn",
     "ar": "وذلك لأن أصلها أن تكون بمعنى «قد»، كما جاءت على الأصل في قوله تعالى: ﴿هل أتى على الإنسان حين من الدهر﴾[[١]] أي: قد أتى،",
     "en": "that is because its origin is to be in the sense of “qad”, as it comes in its original sense in His words, the Exalted: “Has there come upon man a period of time…”, that is: there has come;"},
    {"type": "matn",
     "ar": "فلما كان أصلها «قد»، وهي من لوازم الأفعال، فإن رأت فعلا في حيزها تذكرت عهودا بالحمى وحنت إلى الألف المألوف وعانقته،",
     "en": "so, since its origin is “qad”, which is one of the constant companions of verbs, if it sees a verb within its domain it recalls old bonds at the sanctuary, yearns for the familiar companion and embraces it;"},
    {"type": "matn",
     "ar": "وإن لم تره في حيزها تسلت عنه ذاهلة.",
     "en": "and if it does not see it within its domain, it consoles itself, forgetting it."},
    {"type": "matn",
     "ar": "(و«الهمزة» أعم تصرفا) أي: التصرف فيها باعتبار استعمالها في مواضع استعمالاتها أكثر من التصرف في «هل».",
     "en": "(And the “hamza” is more general in its use), that is, the freedom of use in it, with respect to its being used in the places of its uses, is greater than the freedom of use in “hal”."},
    {"type": "matn",
     "ar": "(تقول: «أزيدا ضربت؟») بإدخال الهمزة على الاسم مع وجود الفعل، بخلاف: «هل زيدا ضربت؟» لما عرفت.",
     "en": "(You say: “a-Zaydan ḍarabta?” [was it Zayd you struck?]), entering the hamza upon the noun while a verb is present, unlike “hal Zaydan ḍarabta?”, for the reason you have learned."},
    {"type": "matn",
     "ar": "(و) تقول: («أتضرب زيدا وهو أخوك؟») باستعمال الهمزة لإثبات ما دخلت عليه على وجه الإنكار دون «هل تضرب زيدا؟»؛",
     "en": "(And) you say: (“a-taḍribu Zaydan wa-huwa akhūka?” [do you strike Zayd when he is your brother?]), using the hamza to affirm what it enters upon by way of disapproval (inkār), but not “hal taḍribu Zaydan?”;"},
    {"type": "matn",
     "ar": "لأن المستفهم عنه في مثل هذا الموضع محذوف بالحقيقة؛ لأن أصله: «أترضى بضربك زيدا؟ وهو غير مستحسن منك»،",
     "en": "because what is asked about in such a place is in reality elided, its origin being: “Are you content with your striking Zayd, when that is not approved of from you?”;"},
    {"type": "matn",
     "ar": "و«هل» ضعيفة في الاستفهام، فلا يحذف فعلها، بخلاف الهمزة، فإنها قوية فيه.",
     "en": "and “hal” is weak in interrogation, so its verb is not elided, unlike the hamza, which is strong in it."},
    {"type": "matn",
     "ar": "(و) تقول: («أزيد عندك أم عمرو؟») بجعل الهمزة معادلة لـ«أم» المتصلة،",
     "en": "(And) you say: (“a-Zaydun ʿindaka am ʿAmrun?” [is Zayd with you, or ʿAmr?]), making the hamza the counterpart of the connected (muttaṣila) “am”;"},
    {"type": "matn",
     "ar": "فإنه لما قصد الاستفهام عن أحد الأمرين تعدد المستفهم عنه، فاستعمال الهمزة التي هي الأصل في باب الاستفهام، والأقوى فيه أنسب وأليق.",
     "en": "for when interrogation about one of two things is intended, what is asked about is multiple, so using the hamza, which is the original and the stronger in the domain of interrogation, is more fitting and more appropriate."},
    {"type": "matn",
     "ar": "وتقع «هل» مع «أم» المنقطعة؛ لأن المستفهم عنه في صورة «أم» المنقطعة لم يتعدد؛",
     "en": "“Hal” does occur with the disconnected (munqaṭiʿa) “am”, because in the case of the disconnected “am” what is asked about is not multiple;"},
    {"type": "matn",
     "ar": "لأنها للإضراب عن السؤال الأول، واستئناف سؤال آخر بـ«أم» المقدرة بالهمزة،",
     "en": "for it serves to turn away (iḍrāb) from the first question and to begin another question with “am”, which is construed as [containing] the hamza,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair", "ar": "سورة الإنسان: ١.", "en": "Qurʾān, Sūrat al-Insān 76:1."},
]
