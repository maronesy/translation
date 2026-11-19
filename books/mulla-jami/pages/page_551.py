# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 551 (printed ٥٥٠)."""

PAGE_NUMBER = 551
PRINTED_PAGE = "٥٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وأما قسم السؤال فلا يتلقى إلا بما فيه من معنى الطلب، نحو: «بالله أخبرني؟» و«بالله هل قام زيد؟».",
     "en": "As for the oath of request, it is met only with something containing the sense of a demand (ṭalab), as in “bi-llāhi akhbirnī?” (by Allah, tell me!) and “bi-llāhi hal qāma Zaydun?” (by Allah, did Zayd stand?)."},
    {"type": "matn",
     "ar": "(و) قد (يحذف جوابه) أي: جواب القسم[[١]] (إذا اعترض) أي: توسط (القسم) بين أجزاء الجملة[[٢]] التي تدل على جواب القسم.",
     "en": "(And its answer) — that is, the answer of the oath — is sometimes (omitted when the oath intervenes), that is, comes in the middle, between the parts of the sentence that indicates the answer of the oath,"},
    {"type": "matn",
     "ar": "(أو تقدمه) أي: القسم (ما يدل عليه) أي: على جوابه نحو: «زيد والله قائم»، و«زيد قائم والله»",
     "en": "(or when what indicates it) — that is, its answer — (precedes it), that is, the oath, as in “Zaydun wa-llāhi qāʾimun” (Zayd, by Allah, is standing) and “Zaydun qāʾimun wa-llāhi” (Zayd is standing, by Allah),"},
    {"type": "matn",
     "ar": "لاستغنائه عن الجواب في هاتين الصورتين، لوجود ما يدل عليه.",
     "en": "because it dispenses with the answer in these two cases, since there is something that indicates it."},
    {"type": "matn",
     "ar": "والجملة المذكورة وإن كانت جوابا للقسم بحسب المعنى، لكنه بحسب اللفظ لا يسمى إلا الدال على الجواب[[٣]] لا الجواب[[٤]]،",
     "en": "The sentence mentioned, even though it is the answer of the oath in meaning, is nevertheless called, in respect of the wording, only “that which indicates the answer”, not the answer [itself];"},
    {"type": "matn",
     "ar": "ولهذا لا يجب فيها علامة جواب القسم[[٥]].",
     "en": "for this reason the mark of the answer of the oath is not required in it."},

    {"type": "section", "ar": "[عن]",
     "en": "ʿAn"},

    {"type": "matn",
     "ar": "(وعن للمجاوزة) أي: لمجاوزة شيء وتعديته عن شيء آخر، وذلك:",
     "en": "(And ʿan is for passing beyond (mujāwaza)), that is, for something’s passing beyond and moving away from another thing; and that is"},
    {"type": "matn",
     "ar": "١-إما بزواله عن الشيء الثاني ووصوله إلى الثالث، نحو: «رميت السهم عن القوس إلى الصيد».",
     "en": "1. either by its departing from the second thing and reaching a third, as in “ramaytu al-sahma ʿan al-qawsi ilā al-ṣaydi” (I shot the arrow from the bow at the game);"},
    {"type": "matn",
     "ar": "٢-أو بالوصول وحده نحو: «أخذت عنه العلم».",
     "en": "2. or by reaching alone, as in “akhadhtu ʿanhu al-ʿilma” (I took knowledge from him);"},
    {"type": "matn",
     "ar": "٣-أو بالزوال وحده نحو: «أديت عنه الدين».",
     "en": "3. or by departing alone, as in “addaytu ʿanhu al-dayna” (I paid the debt on his behalf)."},

    {"type": "section", "ar": "[على]",
     "en": "ʿAlā"},

    {"type": "matn",
     "ar": "(وعلى للاستعلاء) أي: لاستعلاء شيء على شيء[[٦]]، نحو: «زيد على السطح»، و«عليه دين».",
     "en": "(And ʿalā is for superiority (istiʿlāʾ)), that is, for one thing’s being above another, as in “Zaydun ʿalā al-saṭḥi” (Zayd is on the roof) and “ʿalayhi daynun” (he is under a debt)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الجملة التي يؤتى لأجلها بالقسم كان القسم بطلبها كالسؤال للجواب.",
     "en": "That is, the sentence for whose sake the oath is brought; the oath, in requiring it, is like a question in requiring an answer."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "تنازع «اعترض» و«تقدم» في ما يدل عليه، فأعمل تقدم، وحذف معمول «اعترض»، وإليه أشار الشارح.",
     "en": "“Iʿtaraḍa” and “taqaddama” contend (tanāzuʿ) over “mā yadullu ʿalayhi” (what indicates it); he made “taqaddama” govern it and omitted the governed term of “iʿtaraḍa”, and the commentator pointed to this."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لاقتضاء القسم الصدارة، لكونه إنشاء.",
     "en": "Because the oath requires the initial position (ṣadāra), since it is a performative (inshāʾ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مجامعة لا مع النفي والاستثناء، قد تقع في تراكيب المصنفين للتنصيص على المقصود،",
     "en": "The combination of “lā” with negation and exception occurs at times in the constructions of authors, to state the intended meaning explicitly,"},
    {"type": "pair",
     "ar": "وإن لم تقع في كلام البلغاء الذين يستشهد بكلامهم، نص عليه في المطول.",
     "en": "even though it does not occur in the speech of the eloquent whose speech is cited as evidence; this is stated explicitly in al-Muṭawwal."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "من الأمور المذكورة، فلا يرد نقضا على ما ذكر؛ لأنه ليس جواب القسم.",
     "en": "[That is,] of the matters mentioned; so it is not brought as a counter-example to what has been stated, because it is not the answer of the oath."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إما حقيقة كما في المثال الأول، أو مجازا كما في المثال الثاني، كأنه تحمل ثقل الدين على عنقه أو ظهره.",
     "en": "Either literally, as in the first example, or figuratively, as in the second example, as though he bore the weight of the debt on his neck or his back."},
]
