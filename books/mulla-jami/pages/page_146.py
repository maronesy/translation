# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 146 (printed ١٤٥)."""

PAGE_NUMBER = 146
PRINTED_PAGE = "١٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "على تقدير إعماله: إما الإضمار قبل الذكر كما هو مذهب الجمهور، أو حذف الفاعل كما هو مذهب الكسائي،",
     "en": "…on the supposition of making it govern, either concealment before mention, as is the doctrine of the majority, or elision of the agent, as is the doctrine of al-Kisāʾī;"},
    {"type": "matn",
     "ar": "بل يجب عنده إعمال الفعل الأول، فإن اقتضى الثاني الفاعل أضمرته، وإن اقتضى المفعول حذفته أو أضمرته،",
     "en": "rather, according to him, making the first verb govern is obligatory; then if the second requires the agent you conceal it, and if it requires the object you elide it or conceal it."},
    {"type": "matn",
     "ar": "تقول: «ضربني وأكرماني الزيدان»، «ضربني وأكرمت الزيدان»، «ضربني وأكرمتهما الزيدان»، ولا يلزم حينئذ محذور.",
     "en": "You say: “The two Zayds struck me and honored me” (ḍarabanī wa-akramānī al-Zaydān), “ḍarabanī wa-akramtu al-Zaydān,” “ḍarabanī wa-akramtuhumā al-Zaydān”; and in that case nothing objectionable is entailed."},
    {"type": "matn",
     "ar": "وقيل: روي عنه تشريك الرافعين[[١]] أو إضماره بعد الظاهر كما في صورة تأخير الناصب،",
     "en": "It has been said: there is reported from him [al-Farrāʾ] the sharing [of the noun] by the two nominative-governors, or its concealment after the overt [noun], as in the case where the accusative-governor is placed later;"},
    {"type": "matn",
     "ar": "تقول: «ضربني وأكرمني زيد هو»، و«ضربني وأكرمت زيدا هو»، ورواية المتن غير مشهورة عنه.",
     "en": "you say: “Zayd struck me and honored me—he” (ḍarabanī wa-akramanī Zaydun huwa), and “He struck me and I honored Zayd—he”; but the report in the base text is not the well-known one from him."},
    {"type": "matn",
     "ar": "(وحذفت المفعول) تحرزا عن التكرار[[٢]] لو ذكر، وعن الإضمار قبل الذكر في الفضلة لو أضمر",
     "en": "(And you elide the object—wa-ḥadhafta al-mafʿūl), guarding against repetition were it mentioned, and against concealment before mention in a non-essential constituent (faḍla) were it concealed,"},
    {"type": "matn",
     "ar": "(إن استغني عنه[[٣]] وإلا) أي: وإن لم يستغن عنه (أظهرت) أي: المفعول،",
     "en": "(if it can be dispensed with; otherwise—in ustughniya ʿanhu wa-illā), that is: if it cannot be dispensed with, (you make [it] overt—aẓharta), that is: the object,"},
    {"type": "matn",
     "ar": "نحو: «حسبني منطلقا وحسبت زيدا منطلقا»؛",
     "en": "as in: “Zayd deemed me setting off, and I deemed him setting off” (ḥasibanī munṭaliqan wa-ḥasibtu Zaydan munṭaliqan);"},
    {"type": "matn",
     "ar": "لأنه لا يجوز حذف أحد مفعولي باب «حسبت»[[٤]]، ولا يجوز إضماره؛ لئلا يلزم الإضمار قبل الذكر في الفضلة[[٥]].",
     "en": "because eliding one of the two objects of the class of “ḥasibtu” is not permissible, nor is concealing it permissible, lest concealment before mention in a non-essential constituent be entailed."},
    {"type": "matn",
     "ar": "(وإن أعملت الفعل الأول) كما هو مختار الكوفيين (أضمرت الفاعل في) الفعل (الثاني) لو اقتضاه،",
     "en": "(And if you make the first verb govern—wa-in aʿmalta al-fiʿla al-awwal), as is the choice of the Kūfans, (you conceal the agent in the second) verb (aḍmarta al-fāʿila fī al-thānī), if it requires it,"},
    {"type": "matn",
     "ar": "نحو: «ضربني وأكرمني زيد» إذا جعلت «زيد» فاعل «ضربني»، وأضمرت في «أكرمني» ضميرا راجعا إلى «زيد» لتقدمه رتبة،",
     "en": "as in: “Zayd struck me and honored me,” when you make “Zayd” the agent of “ḍarabanī” and conceal in “akramanī” a pronoun referring back to “Zayd,” because it precedes in rank;"},
    {"type": "matn",
     "ar": "فلا محذور فيه حينئذ: لا حذف الفاعل ولا الإضمار قبل الذكر لفظا ورتبة، بل لفظا فقط وهو جائز،",
     "en": "so in that case there is nothing objectionable in it: neither elision of the agent nor concealment before mention in both wording and rank, but only in wording, which is permissible."},
    {"type": "matn",
     "ar": "(وأضمرت المفعول في) الفعل (الثاني) لو اقتضاه (على) المذهب (المختار[[٦]]) ولم تحذفه وإن",
     "en": "(And you conceal the object in the second) verb (wa-aḍmarta al-mafʿūla fī al-thānī), if it requires it, (according to the preferred—ʿalā al-mukhtār) doctrine, and you do not elide it, even if…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيلزم توارد العلتين على معلول واحد، وذلك غير جائز،",
     "en": "So the convergence of two causes upon a single effect would be entailed, and that is not permissible;"},
    {"type": "pair",
     "ar": "وذلك لأن العوامل النحوية بمنزلة المؤثرات الحقيقية عندهم.",
     "en": "that is because grammatical governors have the status of real efficient causes according to them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: تكرار الاسم المتنازع فيه وإن كان فاعلا في إحدى المرتين، ومفعولا في الأخرى.",
     "en": "That is: repetition of the noun contended over, even if it is agent in one of the two occurrences and object in the other."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "شرط استغنى عن الجزاء لتقدم ما يدل عليه.",
     "en": "A condition that dispenses with an apodosis because what indicates it has preceded."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن مفعوله بالحقيقة مضمون المفعولين؛ لأنه متعلق الحسبان والعلم، فلو حذف أحد مفعوليه لزم حذف بعض الأجزاء لمفعول واحد.",
     "en": "Because its object in reality is the content of the two objects, since that is what supposition and knowledge attach to; so were one of its two objects elided, the elision of some of the parts of a single object would be entailed."},
    {"type": "pair",
     "ar": "واعترض عليه بأنه يجوز في السعة وغيرها وإن كان قليلا؛ لأن كلا منهما في الظاهر مفعول برأسه.",
     "en": "It has been objected that it is permissible in ordinary usage (al-saʿa) and elsewhere, even if rare, because each of the two is outwardly an object in its own right."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا بد أن يقول: والفصل الكثير بين الفعل ومفعوله لشديد الاقتضاء له لئلا يتجه عليه أنه فليؤخر الضمير عن الظاهر.",
     "en": "He must say: “and the long separation between the verb and its object, owing to the strong requirement [of the verb] for it,” so that the objection does not arise against him: “then let the pronoun be placed after the overt [noun].”"},
    {"type": "pair",
     "ar": "ولا يخفى أن الإضمار أو التكرار أو الفصل لازم في التقدير، فالمقصود الاحتراز عن التصريح وإخفاء ما هو لازم من القبيح.",
     "en": "It is not hidden that concealment, repetition or separation is entailed in the underlying structure (al-taqdīr); so the purpose is to avoid explicit statement and to conceal what is entailed of the unseemly."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى على الاستعمال المختار. وكأنه أراد بالمذهب الاستعمال.",
     "en": "It would be better [to say] “according to the preferred usage.” It is as if he meant by “doctrine” usage."},
]
