# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 533 (printed ٥٣٢)."""

PAGE_NUMBER = 533
PRINTED_PAGE = "٥٣٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وهما) أي: فعلا التعجب[[١]] (غير متصرفين) فلا يتغيران إلى مضارع ومجهول وتأنيث.",
     "en": "(And the two), that is, the two verbs of wonder, (are not inflectable (ghayr mutaṣarrifayn)): they do not change into a muḍāriʿ, a passive or a feminine."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «وهي -أي: أفعال التعجب- غير متصرفة».",
     "en": "In some copies: “and they (that is, the verbs of wonder) are not inflectable”."},
    {"type": "matn",
     "ar": "(مثل: «ما أحسن زيدا»، و«أحسن بزيد»).",
     "en": "(As in “mā aḥsana Zaydan” (how handsome Zayd is!) and “aḥsin bi-Zaydin” (how handsome Zayd is!).)"},
    {"type": "matn",
     "ar": "(ولا يبنيان) أي: فعلا التعجب (إلا مما يبنى منه أفعل التفضيل لمشابهتهما له) من حيث إن كلا منهما للمبالغة والتأكيد[[٢]]،",
     "en": "(And they), that is, the two verbs of wonder, (are formed only from what the elative (afʿal al-tafḍīl) is formed from, because of their resemblance to it), in that each of them is for intensification and emphasis;"},
    {"type": "matn",
     "ar": "وكذا لا يبنيان إلا للفاعل كأفعل التفضيل، وقد شذ: «ما أشهى الطعام»[[٣]]، و«ما أمقت الكذب».",
     "en": "and likewise they are formed only for the agent, like the elative. “Mā ashhā al-ṭaʿāma” (how desirable food is!) and “mā amqata al-kadhiba” (how hateful lying is!) are anomalous."},
    {"type": "matn",
     "ar": "(ويتوصل في) الفعل (الممتنع) بناء صيغتي التعجب منه من رباعي أو ثلاثي مزيد فيه أو ثلاثي مجرد، مما فيه لون أو عيب",
     "en": "(And in) the verb (from which it is impossible) to form the two forms of wonder, whether quadriliteral, augmented triliteral, or bare triliteral denoting a colour or a defect, (one reaches [the construction]"},
    {"type": "matn",
     "ar": "(بمثل: «ما أشد استخراجه»، و«أشدد باستخراجه») أي: يتوصل ببنائهما من فعل لا يمتنع بناؤهما منه، وجعل[[٤]] الممتنع مفعولا أو مجرورا بالباء.",
     "en": "by such as “mā ashadda istikhrājahu” (how intense his extracting is!) and “ashdid bi-stikhrājihi”), that is, one reaches it by forming the two from a verb from which their formation is not impossible, and making the impossible [verb] an object or governed in the genitive by bāʾ."},
    {"type": "matn",
     "ar": "(ولا يتصرف فيهما) أي: في صيغتي التعجب (بتقديم) أي: تقديم جائز فيما عدا صيغتي التعجب، كتقديم المفعول أو الجار والمجرور على الفعل",
     "en": "(And there is no free handling of the two), that is, of the two forms of wonder, (by placing first), that is, a placing first which is permitted in what is other than the two forms of wonder, like placing the object, or the preposition and its object, before the verb,"},
    {"type": "matn",
     "ar": "(وتأخير) أي: تأخير جائز فيما عداهما كتأخير الفعل منهما،",
     "en": "(or placing after), that is, a placing after which is permitted in what is other than them, like placing the verb after them."},
    {"type": "matn",
     "ar": "وإنما قيدنا التقديم والتأخير بما قيدنا؛ ليكون عدم التصرف بهما من خواص صيغتي التعجب، فإن المقام يقتضي بيان الأحكام الخاصة بهما،",
     "en": "We have qualified placing first and placing after as we did only so that the absence of free handling by them be one of the properties of the two forms of wonder, for the context requires setting out the rules specific to them."},
    {"type": "matn",
     "ar": "فلا يقال: «ما زيدا أحسن»، ولا «بزيد أحسن»؛ لأنهما بعد النقل إلى التعجب جريا مجرى الأمثال، فلا يتغيران كما لا تتغير الأمثال[[٥]].",
     "en": "So one does not say “mā Zaydan aḥsana”, nor “bi-Zaydin aḥsin”; because after their transfer to [expressing] wonder they have run the course of proverbs, and so they do not change, just as proverbs do not change."},
    {"type": "matn",
     "ar": "قيل: عدم التصرف بالتقديم يستلزم عدم التصرف بالتأخير وبالعكس؛",
     "en": "It has been said: the absence of free handling by placing first entails the absence of free handling by placing after, and vice versa;"},
    {"type": "matn",
     "ar": "لأن تقديم الشيء يستلزم تأخير غيره، وكذا تأخيره يستلزم تقديم غيره، فلو اكتفى بأحدهما لكفى.",
     "en": "because placing a thing first entails placing something else after it, and likewise placing it after entails placing something else first; so had he been content with one of them, it would have sufficed."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أشار إلى أن رجوع الضمير المذكور إلى صيغتين مبني على تأويلهما بالفعلين، ولعدم الاحتياج إلى التأويل فسر الضمير المجرور في قوله: فيهما بصيغتي التعجب.",
     "en": "He indicated that the reference of the pronoun mentioned to “two forms” rests on interpreting them as the two verbs; and because no interpretation is needed, he explained the genitive pronoun in his words “fīhimā” (in the two) as the two forms of wonder."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «كما له في الفضل تحققه» (with a space after «كما»); the sense may be «كماله في الفضل وتحققه». Transcribed as printed.
    {"type": "pair",
     "ar": "فإن المقصود من إنشاء التعجب في قولنا: «ما أحسن زيد» إثبات الحسن له على وجه الكمال والتقرير، وكذا المقصود من «زيد أفضل القوم» كما له في الفضل تحققه.",
     "en": "For the purpose of the performative expression of wonder in our saying “mā aḥsana Zayd” is to affirm beauty of him in the mode of perfection and establishment; and likewise the purpose of “Zaydun afḍalu al-qawmi” (Zayd is the most excellent of the people) is the realization of his perfection in excellence."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "في القاموس: شهيه كرضيه أحبه، ورغب فيه، ومقته أبغضه.",
     "en": "In al-Qāmūs: shahiyahu, like raḍiyahu, means he loved it and desired it; and maqatahu means he hated it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بصيغة المصدر عطف على «بنائهما»، وإنما جعل الممتنع ههنا مفعولا، وفي «أفعل» التفضيل تمييزا؛",
     "en": "[Jaʿl], in the form of the verbal noun, coordinated with “bināʾihimā” (their formation). The impossible [verb] is made an object here, and a specification (tamyīz) with the elative “afʿal”,"},
    {"type": "pair",
     "ar": "لأن اسم التفضيل لا يعمل في الفاعل والمفعول به الظاهرين، بخلاف فعل التعجب.",
     "en": "only because the elative does not govern an explicit agent or direct object, unlike the verb of wonder."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "في الكشاف: «المثل» في الأصل بمعنى: المثل والنظير. ثم قيل: للقول السائر الممثل مضربه بمورده،",
     "en": "In al-Kashshāf: “mathal” originally means likeness and counterpart (al-mithl wa-l-naẓīr). Then it was said of a current saying whose occasion of application is likened to its original occasion;"},
    {"type": "pair",
     "ar": "ولم يضربوا مثلا إلا قولا فيه غرابة من بعض الوجوه، ومن ثم حفظ من التغير.",
     "en": "and they did not coin a proverb except from a saying with something unusual about it in some respect; hence it was preserved from change."},
]
