# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 540 (printed ٥٣٩)."""

PAGE_NUMBER = 540
PRINTED_PAGE = "٥٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أو لأن أثرها» at the foot of PDF p. 539 (mid-sentence).
    {"type": "matn",
     "ar": "فيما يليه الجر.",
     "en": "…on what follows them is the genitive (jarr)."},
    {"type": "matn",
     "ar": "(وهي) أي: حروف الجر («من، وإلى، وحتى، وفي») ذكر هذه الحروف على سبيل الحكاية؛ لأنها ليس لها أسماء خاصة يعبر بها عنها.",
     "en": "(And they), that is, the prepositions, (are “min”, “ilā”, “ḥattā”, “fī”); he mentioned these particles by quoting them, because they have no particular names by which they are expressed."},
    {"type": "matn",
     "ar": "(«والباء واللام») ذكرهما باسميهما لوجودهما، وكذلك ذكر الواو والتاء والكاف بأسمائها حيث وجدت، بخلاف ما بقي منها.",
     "en": "(“the bāʾ and the lām”): he mentioned these two by their names because such names exist; likewise he mentioned the wāw, the tāʾ and the kāf by their names, since they exist, unlike the rest of them."},
    {"type": "matn",
     "ar": "(«ورب وواوها») أي: الواو التي تقدر بعدها «رب»، وفي عدها[[١]] من حروف الجر تسامح[[٢]].",
     "en": "(“rubba and its wāw”), that is, the wāw after which “rubba” is supplied; in counting it among the prepositions there is laxity of expression."},
    {"type": "matn",
     "ar": "(و«واو القسم، وتاؤه، وباؤه، وعن، وعلى، والكاف، ومذ، ومنذ، وخلا، وعدا، وحاشا»).",
     "en": "(and “the wāw of the oath, its tāʾ and its bāʾ, ʿan, ʿalā, the kāf, mudh, mundhu, khalā, ʿadā and ḥāshā”)."},
    {"type": "matn",
     "ar": "فالعشرة الأول لا تكون إلا حرفا.",
     "en": "The first ten are only ever particles."},
    {"type": "matn",
     "ar": "والخمسة التي تليها تكون حرفا واسما.",
     "en": "The five that follow them are both particle and noun."},
    {"type": "matn",
     "ar": "والثلاثة البواقي تكون فعلا وحرفا.",
     "en": "The remaining three are both verb and particle."},

    {"type": "section", "ar": "[من]",
     "en": "Min"},

    {"type": "matn",
     "ar": "١-(فـ«من» للابتداء) أي: لابتداء الغاية[[٣]].",
     "en": "1. (“Min” is for beginning), that is, for the beginning of the extent (ibtidāʾ al-ghāya)."},
    {"type": "matn",
     "ar": "والمراد بالغاية: المسافة إطلاقا لاسم الجزء على الكل؛ إذ لا معنى لابتداء النهاية.",
     "en": "What is meant by ghāya is the distance, applying the name of the part to the whole, since “the beginning of the end” has no meaning."},
    {"type": "matn",
     "ar": "وقيل: كثيرا ما يطلقون الغاية[[٤]]، ويريدون بها الغرض والمقصود.",
     "en": "It has been said: they often use ghāya and mean by it the aim and purpose."},
    {"type": "matn",
     "ar": "فالمراد بها الفعل؛ لأنه غرض الفاعل ومقصوده.",
     "en": "So what is meant by it is the act, because it is the aim and purpose of the agent."},
    {"type": "matn",
     "ar": "وهذا الابتداء إما من المكان نحو: «سرت من البصرة» أو من الزمان، نحو: «صمت",
     "en": "This beginning is either from a place, as in “I travelled from Baṣra”, or from a time, as in “I fasted…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: على مذهب سيبويه. وأما على مذهب الأخفش والكوفيين فهي بمعنى «رب» جارة بنفسها.",
     "en": "That is, according to the doctrine of Sībawayh. According to the doctrine of al-Akhfash and the Kūfans, it has the sense of “rubba” and governs the genitive by itself."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولذا لم يجمع واو القسم معها، كما جمع باؤه مع الباآت فرقا بين المعدود مسامحة، والمعدود حقيقة.",
     "en": "For this reason he did not put the wāw of the oath together with it, as he put its bāʾ together with the bāʾs, to distinguish what is counted by laxity from what is counted in reality."},
    {"type": "pair",
     "ar": "والأظهر أنه اختار مذهب الكوفيين، ولم يجمعها مع واو القسم للتصريح بأنها جارة عنده،",
     "en": "The more evident view is that he adopted the doctrine of the Kūfans, and did not put it together with the wāw of the oath in order to state explicitly that in his view it governs the genitive;"},
    {"type": "pair",
     "ar": "ولذا لم يذكر الفاء، وبل مع أن «رب» مضمر بعدها أيضا.",
     "en": "and for this reason he did not mention the fāʾ and “bal”, even though “rubba” is concealed after them too."},
    {"type": "pair",
     "ar": "ولا يضمر بدون هذه الأحرف الثلاثة في الشعر أيضا إلا شاذا.",
     "en": "Nor is it concealed without these three particles, even in poetry, except anomalously."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فاللام للعهد، أو عوض عن المضاف إليه على اختلاف الرأيين.",
     "en": "So the lām [of al-ghāya] is for definite reference, or a substitute for the second term of the annexation, according to the two differing views."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «ولا يصح على القدر من أول النهار إلى آخره»; «القدر» is clear but the phrase is elliptical. Transcribed as printed.
    {"type": "pair",
     "ar": "فيه أنه يلزم أن يخص من الابتدائية بالأفعال الاختيارية التي لها غرض، ولا يصح على القدر من أول النهار إلى آخره.",
     "en": "Against this: it would follow that the min of beginning is restricted to voluntary acts that have an aim, and it would not be valid for the measure “from the beginning of the day to its end”."},
    {"type": "pair",
     "ar": "والأحسن أن المراد بالغاية النهاية أي: الابتداء له نهاية، ولا يستعمل في الابتداء لا نهاية له كالأمور الأبدية.",
     "en": "Better is that what is meant by ghāya is the end; that is, a beginning that has an end; it is not used for a beginning that has no end, such as everlasting things."},
    {"type": "pair",
     "ar": "وأما تفسير الغاية بمعنى المسافة، فيوجب أن يكون استعماله في الزمان مجازا إلا أن يراد بالمسافة الحقيقية أو التنزيلية.",
     "en": "As for explaining ghāya in the sense of distance, it requires that its use for time be figurative, unless what is meant by distance is real or notional distance."},
]
