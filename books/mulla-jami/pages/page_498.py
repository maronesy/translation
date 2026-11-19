# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 498 (printed ٤٩٧)."""

PAGE_NUMBER = 498
PRINTED_PAGE = "٤٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(إذا كان المعطوف عليه اسما صريحا)،» at the foot of PDF p. 497.
    {"type": "matn",
     "ar": "نحو: «أعجبني ضربك زيدا وتشتم، أو فتشتم، أو ثم تشتم»، فـ«ثم» ليست من الحروف المذكورة، وتقدير «أن» بعد الواو والفاء ليس مشروطا بالشروط المذكورة فيهما.",
     "en": "…as in “aʿjabanī ḍarbuka Zaydan wa-tashtuma” (your striking Zayd and reviling pleased me), or “fa-tashtuma”, or “thumma tashtuma”; “thumma” is not among the particles mentioned, and supposing “an” after the wāw and the fāʾ is not here conditional on the conditions mentioned for them."},
    {"type": "matn",
     "ar": "فقوله: «والعاطفة إذا كان مرفوعا» فهو معطوف على أول المعدودات الناصبة بتقدير «أن» أعني قوله: «حتى إذا كان مستقبلا»، أو على آخرها وهو: «أو بشرط معنى: إلى أن».",
     "en": "So his words “wa-l-ʿāṭifa”, if [the word] is in the nominative, are coordinated upon the first of the enumerated items that put [the verb] in the accusative by supposing “an”, namely his words “ḥattā, when it is future”, or upon the last of them, namely “and aw, on condition of the sense of ilā an.”"},
    {"type": "matn",
     "ar": "وقيل: هو مجرور معطوف على «حتى» في قوله: «وبأن مقدرة بعد حتى»،",
     "en": "It has also been said that it is in the genitive, coordinated upon “ḥattā” in his words “and by an supposed after ḥattā.”"},
    {"type": "matn",
     "ar": "وظاهر أن هذا وإن كان أبعد بحسب اللفظ[[١]]، لكنه أقرب بحسب المعنى؛",
     "en": "It is evident that this, though more remote in wording, is nearer in meaning;"},
    {"type": "matn",
     "ar": "لأنه على التقدير الأول إن جعل العاطفة أعم مما ذكر -كما ذكرنا- يلزم[[٢]] أن يذكر في التفصيل ما لم يكن في الإجمال،",
     "en": "because on the first construal, if “the coordinating [particle]” is taken as more general than what was mentioned, as we have said, it follows that something is mentioned in the detailed account that was not in the summary;"},
    {"type": "matn",
     "ar": "وإن خصت به يلزم تخصيص الحكم به، وليس في الواقع مخصوصا به لما سبق من جريانه في «ثم» أيضا.",
     "en": "and if it is restricted to it, it follows that the ruling is restricted to it, whereas in fact it is not restricted to it, given what preceded about its applying to “thumma” as well."},
    {"type": "matn",
     "ar": "ويرد عليه: أنه كان المناسب حينئذ ذكرها مرتين: مرة في الإجمال، ومرة في التفصيل، كسائر ما ذكرناه.",
     "en": "Against this it is objected that it would then have been fitting to mention it twice, once in the summary and once in the detailed account, like the rest of what we have mentioned."},
    {"type": "matn",
     "ar": "(ويجوز إظهار «أن» مع «لام» كي) نحو: «جئتك لأن تكرمني»، (ومع ما ألحق بها) من اللام الزائدة، نحو: «أردت لأن تقوم».",
     "en": "(And “an” may be made explicit with the “lām” of kay), as in “jiʾtuka li-an tukrimanī” (I came to you so that you might honour me), (and with what is assimilated to it), namely the redundant lām, as in “aradtu li-an taqūma” (I wanted you to stand)."},
    {"type": "matn",
     "ar": "(و) مع الحروف (العاطفة[[٣]]) نحو: «أعجبني قيامك[[٤]] وأن تذهب»؛",
     "en": "(And) with the (coordinating) particles, as in “aʿjabanī qiyāmuka wa-an tadhhaba” (your standing and your going pleased me);"},
    {"type": "matn",
     "ar": "لأن هذه الثلاثة تدخل على اسم صريح نحو: «جئتك للإكرام، وأعجبني ضرب زيد وغضبه، وأردت لضربك»،",
     "en": "because these three enter upon an explicit noun, as in “I came to you for the honouring”, “Zayd’s striking and his anger pleased me”, and “I wanted your striking”;"},
    {"type": "matn",
     "ar": "فجاز «أن» يظهر معها ما يقلب الفعل إلى اسم صريح، وهو «أن» المصدرية.",
     "en": "so it is permissible that there appear with them what turns the verb into an explicit noun, namely the infinitival “an” (an al-maṣdariyya)."},
    {"type": "matn",
     "ar": "وأما «لام» الجحود: فلما لم يدخل على الاسم الصريح لم يظهر بعدها «أن»،",
     "en": "As for the “lām” of denial, since it does not enter upon an explicit noun, “an” does not appear after it;"},
    {"type": "matn",
     "ar": "وكذا «حتى»؛ لأن الأغلب فيها أن تستعمل بمعنى «كي» وهي بهذا المعنى لا تدخل",
     "en": "and likewise “ḥattā”, because it is mostly used in the sense of “kay”, and in this sense it does not enter…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "للزوم الفصل بتفصيل الحروف السابقة وإن لم يكن أجنبيا.",
     "en": "Because of the separation that results from the detailed account of the preceding particles, even if it is not extraneous."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «لا خير»; the following «إنما الضرر» suggests «لا ضير» (no harm). Transcribed as printed.
    {"type": "pair",
     "ar": "لا خير في كون التفصيل مشتملا على معنى زائد على الإجمال إنما الضرر في كونه قاصرا عن إفادة التفصيل لما أجمل.",
     "en": "There is no harm in the detailed account containing a meaning beyond the summary; the harm lies only in its falling short of conveying the detail of what was summarized."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: مع العاطفة مطلقا إذا قدر أن بعدها بالشرط المشترك بين الكل بخلاف العاطفة المقدر أن بعدها بشرط مخصوص كما فصل في «حتى» وأخواتها،",
     "en": "That is, with the coordinating [particle] without restriction, when “an” is supposed after it under the condition common to all; unlike the coordinating [particle] after which “an” is supposed under a specific condition, as detailed for “ḥattā” and its sisters."},
    {"type": "pair",
     "ar": "وهو المتبادر من قوله: والعاطفة؛ لأن هذه الحروف ذكرت بهذه العبارة حين بيان الشرط المشترك بين الكل.",
     "en": "This is what first comes to mind from his words “and the coordinating [particle]”, because these particles were mentioned with this expression when the condition common to all was set out."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار بالمثال إلى أن المراد العاطفة المذكورة سابقا، وهي ما يكون قبلها اسم صريح.",
     "en": "By the example he indicated that what is meant is the coordinating [particle] mentioned earlier, namely one before which there is an explicit noun."},
]
