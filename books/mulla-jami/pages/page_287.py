# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 287 (printed ٢٨٦)."""

PAGE_NUMBER = 287
PRINTED_PAGE = "٢٨٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وبعد» from the foot of PDF p. 286.
    {"type": "matn",
     "ar": "«حاشا» في الأكثر) لكونها حرف جر[[١]] في أكثر استعمالاتهم،",
     "en": "…“ḥāshā” in most [usage]), because it is a preposition (ḥarf jarr) in most of their usages;"},
    {"type": "matn",
     "ar": "وأجاز بعضهم النصب بها على أنها فعل متعد فاعله مضمر، ومعناها تبرئة المستثنى[[٢]] عما نسب إلى المستثنى منه،",
     "en": "some permitted the accusative after it, on the view that it is a transitive verb whose agent is concealed, its meaning being to clear the excepted of what is attributed to the excepted-from,"},
    {"type": "matn",
     "ar": "نحو: «ضرب القوم عمرا حاشا زيدا» أي: برأه الله عن ضرب عمرو.",
     "en": "as in “The people struck ʿAmr, ḥāshā Zaydan,” that is, God cleared him of striking ʿAmr."},
    {"type": "matn",
     "ar": "(وإعراب «غير» فيه) أي: في الاستثناء دون الصفة؛ إذ هو حينئذ يعرب بإعراب موصوفه",
     "en": "(The inflection of “ghayr” in it), that is, in exception, not as an attribute—since in that case it is inflected with the inflection of what it qualifies—"},
    {"type": "matn",
     "ar": "(كإعراب المستثنى بـ«إلا» على التفصيل) المذكور فيما سبق، فكأنه لما انجر به المستثنى للإضافة انتقل إعرابه إليه[[٣]].",
     "en": "(is like the inflection of what is excepted by “illā,” according to the detailed account) given above; it is as though, when the excepted was put in the genitive by it through annexation (iḍāfa), its inflection passed over to it."},
    {"type": "matn",
     "ar": "(و«غير») أي: كلمة «غير» في الأصل (صفة[[٤]]) لدلالتها على ذات مبهمة باعتبار قيام معنى المغايرة بها،",
     "en": "(And “ghayr”), that is, the word “ghayr,” is originally (an attribute [ṣifa]), because it denotes an indeterminate essence considered as bearing the sense of otherness (mughāyara);"},
    {"type": "matn",
     "ar": "فالأصل فيها أن تقع صفة كما تقول: «جاءني رجل غير زيد»، واستعمالها على هذا الوجه كثير في كلام العرب،",
     "en": "so its basic use is to occur as an attribute, as you say “A man other than Zayd came to me”; and its use in this way is frequent in the speech of the Arabs."},
    {"type": "matn",
     "ar": "لكنها (حملت على «إلا») واستعملت مثلها (في الاستثناء) على خلاف الأصل، وذلك لاشتراك كل منهما في مغايرة ما بعده لما قبله",
     "en": "But it (was assimilated to “illā”) and used like it (in exception), contrary to its basic use; that is because each of them shares in [expressing] the otherness of what follows it from what precedes it,"},
    {"type": "matn",
     "ar": "(كما حملت «إلا» عليها) أي: على كلمة «غير» (في الصفة) لكن لا يحمل «إلا» عليها في الصفة غالبا",
     "en": "(just as “illā” was assimilated to it), that is, to the word “ghayr,” (in [serving as] an attribute); but “illā” is not usually assimilated to it as an attribute"},
    {"type": "matn",
     "ar": "إلا: (إذا كانت) أي: «إلا» (تابعة لجمع) أي: واقعة بعد متعدد، فوجب أن يكون موصوفها مذكورا[[٥]] لا مقدرا، كما قد يكون مقدرا في «غير» مثل: «جاءني غير زيد»،",
     "en": "except (when it), that is, “illā,” (follows a plural), that is, occurs after a multiple; and its qualified noun must be expressed, not supposed, as it sometimes is supposed with “ghayr,” as in “Someone other than Zayd came to me”;"},
    {"type": "matn",
     "ar": "وبعد ما كان مذكورا يكون متعددا، ليوافق حالها صفة حالها أداة الاستثناء؛ إذ لا بد لها في الاستثناء من مستثنى منه متعدد،",
     "en": "and, being expressed, it must be multiple, so that its state as an attribute accords with its state as a particle of exception; for in exception it must have a multiple excepted-from."},
    {"type": "matn",
     "ar": "فلا تقول في الصفة: «جاءني رجل إلا زيد»،",
     "en": "So you do not say, with it as an attribute, “A man other than Zayd came to me [jāʾanī rajulun illā Zaydun].”"},
    {"type": "matn",
     "ar": "والمتعدد أعم من أن يكون جمعا لفظا كـ«رجال» أو تقديرا كـ«قوم ورهط»، وأن يكون مثنى فدخل فيه نحو: «ما جاءني رجلان إلا زيد[[٦]]».",
     "en": "The multiple is more general than being plural in wording, like “rijāl” (men), or by supposition, like “qawm” and “rahṭ” (people, band), and [includes] being dual; so it covers such as “Two men other than Zayd did not come to me.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وإليه ذهب سيبويه. والدليل على حرفيتها قولهم: حاشاي من دون نون الوقاية،",
     "en": "This is the view of Sībawayh. The evidence that it is a particle is their saying “ḥāshāya” without the protective nūn (nūn al-wiqāya),"},
    {"type": "pair",
     "ar": "وامتناع وقوعها صلة لما المصدرية مطردا، ودخول «ما» عليه، ونصب الاسم بعدها شاذ عنده.",
     "en": "and the impossibility of its regularly occurring as the relative clause of verbal-noun “mā” (mā al-maṣdariyya) and of “mā” entering upon it; and the accusative of the noun after it is anomalous in his view."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فلا يستثنى بها إلا عما نسب إليه سوء.",
     "en": "So it is used to except only from that to which something bad is attributed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فالإعراب حقيقة لما أضيف إليه. ولهذا جاز العطف على محله نحو: ما جاءني غير زيد وعمرو بالرفع؛ لأن المعنى: ما جاءني إلا زيد.",
     "en": "So the inflection in reality belongs to what it is annexed to. For this reason coordination with its place is allowed, as in “None came to me other than Zayd and ʿAmrun” with the nominative, because the meaning is: “None came to me except Zayd.”"},
    {"type": "pair",
     "ar": "قيل: لما كان إعرابه بعينه إعراب المستثنى بـ«إلا» لكان الأحسن أن يقول: وإعراب غير المستثنى بـ«إلا» بدون الكاف.",
     "en": "It has been said: since its inflection is exactly the inflection of what is excepted by “illā,” it would have been better to say “and the inflection of ghayr is the excepted by illā” without the kāf [of comparison]."},
    {"type": "pair",
     "ar": "وإنما لم يبين غير مع أنه بمعنى الحرف؛ لأن ذلك فيه عارض.",
     "en": "“Ghayr” was not made indeclinable, although it has the sense of a particle, only because that [sense] is incidental in it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "غير مبتدأ، وما بعدها خبران له.",
     "en": "“Ghayr” is a subject (mubtadaʾ), and what follows it is two predicates of it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما اشترط ذلك ليكون أظهر في كونها صفة.",
     "en": "He stipulated this only so that it would be more evident that it is an attribute."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا يجوز ههنا الاستثناء المتصل؛ لأن المحكوم عليه إثنان من هذا الجنس، وليس زيد اثنين منه.",
     "en": "Shaykh al-Raḍī said: connected exception (istithnāʾ muttaṣil) is not permitted here, because what is judged about is two of this kind, and Zayd is not two of them."},
]
