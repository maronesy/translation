# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 167 (printed ١٦٦)."""

PAGE_NUMBER = 167
PRINTED_PAGE = "١٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "لإمكان الذهول عن الفتحة[[١]] لخفائها، أو في الكتابة[[٢]] (مثل: «عندي أنك قائم» وجب تقديمه) أي: تقديم الخبر على المبتدأ في جميع هذه الصور، كما ذكرنا.",
     "en": "…since the fatḥa may be overlooked owing to its inconspicuousness—or in writing—“as in: ‘In my view, [it is] that you are standing’ (ʿindī annaka qāʾimun), its placing first is obligatory,” that is, placing the khabar before the mubtadaʾ in all of these cases, as we have mentioned."},

    {"type": "section", "ar": "[ تعدد الخبر ]",
     "en": "The Multiplicity of the Khabar"},

    {"type": "matn",
     "ar": "(وقد يتعدد[[٣]] الخبر) من غير تعدد المخبر عنه[[٤]]، فيكون اثنين فصاعدا، وذلك التعدد:",
     "en": "“The khabar may be multiple,” without the subject of predication (al-mukhbar ʿanhu) being multiple, so that it is two or more. This multiplicity is:"},
    {"type": "matn",
     "ar": "إما بحسب اللفظ والمعنى جميعا[[٥]]، ويستعمل ذلك على وجهين: بالعطف مثل: «زيد عالم وعاقل»، وبغير العطف (مثل: «زيد عالم عاقل»).",
     "en": "either in respect of both wording and meaning together—and this is used in two ways: with conjunction, as in “Zayd is learned and intelligent” (Zaydun ʿālimun wa-ʿāqilun), and without conjunction, “as in: ‘Zayd is learned, intelligent’ (Zaydun ʿālimun ʿāqilun)”;"},
    {"type": "matn",
     "ar": "وإما بحسب اللفظ فقط، نحو: «هذا حلو حامض»، فإنهما في الحقيقة خبر واحد[[٦]]، أي: «مز»[[٧]]، وفي هذه الصورة[[٨]] ترك العطف أولى[[٩]].",
     "en": "or in respect of wording only, as in: “This is sweet, sour” (hādhā ḥulwun ḥāmiḍun); for the two are in reality a single khabar, that is, “sweet-and-sour” (muzz). In this case omitting the conjunction is preferable."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وجواز الحمل على سبق اللسان؛ لأن صدر الكلام موقع «إن» المكسورة.",
     "en": "And because it may be taken as a slip of the tongue, since the head of the utterance is the place of “inna” with kasra."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يعهد رفع لبس الكتابة بالتقديم، نعم يعهد بالزيادة نحو: «عمرو».",
     "en": "Removing a confusion in writing by placing first is not a known practice; it is known, however, [to be done] by an added letter, as in “ʿAmr” (written with a wāw)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لفظة «قد» للتقليل أو للتحقيق.",
     "en": "The word “qad” is for paucity or for affirmation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ومع تعدده أيضا. إما بالعطف نحو: «زيد وعمرو قائم وقاعد»، أو بغير العطف في أحدهما، أو في كليهما، وليس له مثال واقع، بل مجرد احتمال.",
     "en": "And also with its being multiple: either with conjunction, as in “Zayd and ʿAmr are standing and sitting,” or without conjunction in one of the two, or in both; for this there is no attested example, only a bare possibility."},
    {"type": "pair",
     "ar": "ويجوز تعدد المخبر عنه من غير تعدد الخبر، نحو: «زيد وعمرو رجلان، وحلو حامض من الطعوم».",
     "en": "The subject of predication may be multiple without the khabar being multiple, as in: “Zayd and ʿAmr are two men,” and “Sweet [and] sour are among the flavours.”"},
    {"type": "pair",
     "ar": "ولم يتعرض له في جانب المبتدأ لقلته في الكلام.",
     "en": "He did not address it on the side of the mubtadaʾ because of its rarity in speech."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ذلك التعدد: إما غير واجب كما في مثال المتن، أو واجب كقولك: «هما عالم وجاهل»، وحينئذ يجب العطف،",
     "en": "That multiplicity is either not necessary, as in the example of the base text, or necessary, as in your saying “The two of them are learned and ignorant” (humā ʿālimun wa-jāhilun); in that case conjunction is obligatory."},
    {"type": "pair",
     "ar": "وتوجيهه أن يعطف أولا، ثم يجعل المجموع خبرا على إرادة التفصيل اعتمادا على فهم السامع،",
     "en": "Its explanation is that the conjunction is made first, and then the whole is made the khabar, with distribution intended, relying on the hearer's understanding;"},
    {"type": "pair",
     "ar": "وليس في المعطوفين ضمير المبتدأ؛ لأن المبتدأ مفكوك تقديرا، فكأنك قلت في المثال المذكور: «أحدهما عالم، والآخر جاهل»،",
     "en": "and there is no pronoun of the mubtadaʾ in the two conjoined terms, because the mubtadaʾ is notionally separated, as though you said in the example mentioned: “One of them is learned and the other ignorant.”"},
    {"type": "pair",
     "ar": "ولهذا جاز أن يجعله مما نحن فيه؛ لأن المخبر عنه متعدد حقيقة.",
     "en": "For this reason it is permissible to count it among what we are discussing, because the subject of predication is in reality multiple."},
    {"type": "pair",
     "ar": "فعلى هذا جاز أن يكون قوله قدس سره: «من غير تعدد المخبر عنه» احترازا عنه. ويؤيده قوله فيما بعد: «ويستعمل ذلك على وجهين».",
     "en": "Accordingly, his words—may his secret be sanctified—“without the subject of predication being multiple” may be meant to exclude it. This is supported by his words further on: “and this is used in two ways.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأن المقصود إثبات الكيفية المتوسطة.",
     "en": "Because what is intended is to affirm the intermediate quality."},
    {"type": "pair",
     "ar": "فإن قلت: يلزم خلو الحلو مثلا من الضمير، فيكون الخبر المشتق خاليا عن الضمير، على أنه يكذبه وجوب «هذان حلوان حامضان»؟",
     "en": "If you say: it follows that “ḥulw,” for instance, is devoid of a pronoun, so that a derived khabar would be devoid of a pronoun—besides which, the obligatoriness of “hādhāni ḥulwāni ḥāmiḍāni” (these two are sweet, sour) belies it?"},
    {"type": "pair",
     "ar": "قلت: اعتبر في كل منهما ضمير استحقه المجموع، كما أجري على كل إعراب استحقه المجموع.",
     "en": "I say: in each of the two there is taken into account a pronoun which the whole merits, just as an inflection which the whole merits is applied to each."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال في الحاشية: المز الجامع بين الحلاوة والحموضة.",
     "en": "He said in the Ḥāshiya: muzz is what combines sweetness and sourness."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: في صورة تعدد الخبر لفظا فقط ترك العطف أولى لشدة الاتصال بينهما.",
     "en": "That is: in the case of the khabar's being multiple in wording only, omitting the conjunction is preferable because of the close connection between the two."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "هذا إنما يتم فيما إذا لم يتعدد المبتدأ معنى نحو: «هما عالم وجاهل»، فإنه حينئذ العطف واجب؛",
     "en": "This holds only where the mubtadaʾ is not multiple in meaning; [otherwise,] as in “humā ʿālimun wa-jāhilun,” conjunction is then obligatory;"},
    {"type": "pair",
     "ar": "لأنه يجمع المتعدد أولا في هذه الصورة بالعطف، ثم يجعل خبرا،",
     "en": "because in this case the multiple [terms] are first gathered by conjunction and then made the khabar;"},
    {"type": "pair",
     "ar": "ويجب أن يكون هذا الخبر جامدا لفظا أو تقديرا لئلا يلزم خلو الخبر المشتق عن ضمير المبتدأ، فهما عالم وجاهل في تقديرهما: رجل عالم ورجل جاهل.",
     "en": "and this khabar must be non-derived (jāmid) in wording or by implication, lest a derived khabar be devoid of the mubtadaʾ's pronoun; so “ʿālim” and “jāhil” are, in their implied form, “a learned man” and “an ignorant man.”"},
]
