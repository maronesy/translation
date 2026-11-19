# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 428 (printed ٤٢٧)."""

PAGE_NUMBER = 428
PRINTED_PAGE = "٤٢٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ولما غير «الواحد والواحدة» ههنا بدون التركيب[٤]؛ لأن» at the foot of PDF p. 427.
    # REVIEW: «المعطوف إليه» is printed (one would expect «المعطوف عليه»); transcribed as printed.
    # REVIEW: a stray dot is printed after the comma in «التركيب،.لم»; omitted here.
    {"type": "matn",
     "ar": "المعطوف والمعطوف إليه في قوة التركيب، لم يكن استعمالهما بالعطف على صورة لفظ ما تقدم بعينه،",
     "en": "…the conjunct and that to which it is conjoined are equivalent to a compound, their use by conjunction could not be in the very form of the wording of what preceded;"},
    {"type": "matn",
     "ar": "فلذلك لم يدرجهما في قاعدة العطف بلفظ ما تقدم، بل خصها بما عداهما، فقال:",
     "en": "therefore he did not include the two of them in the rule of conjunction with the wording of what preceded, but restricted it to what is other than them, and said:"},
    {"type": "matn",
     "ar": "(ثم بالعطف) أي: بعطف تلك العقود[[١]] على الزائد عليها كائنا ذلك الزائد[[٢]] (بلفظ ما تقدم) من أسماء الأعداد بعينه من غير تغيير،",
     "en": "(then by conjunction), that is, by conjoining those decades to what exceeds them, that excess being (in the wording of what preceded) among the number nouns, exactly, without alteration."},
    {"type": "matn",
     "ar": "فتقول: «اثنان وعشرون» في المذكر، و«اثنتان أو ثنتان وعشرون» في المؤنث، و«ثلاثة وعشرون» في المذكر، و«ثلاث وعشرون» في المؤنث،",
     "en": "So you say “ithnān wa-ʿishrūn” (twenty-two) for the masculine, and “ithnatān” or “thintān wa-ʿishrūn” for the feminine; “thalātha wa-ʿishrūn” (twenty-three) for the masculine, and “thalāth wa-ʿishrūn” for the feminine;"},
    {"type": "matn",
     "ar": "وهكذا (إلى تسعة وتسعين) بل إلى «تسع وتسعين».",
     "en": "and so on (up to tisʿa wa-tisʿīn [ninety-nine]), or rather up to “tisʿ wa-tisʿīn”."},
    {"type": "matn",
     "ar": "(و) تقول فيما زاد على «تسعة وتسعين» (مائة وألف) في الواحد (مائتان وألفان) في التثنية (فيهما) أي: في المذكر والمؤنث من غير فارق بينهما.",
     "en": "(And) you say, for what exceeds “ninety-nine”, (miʾa and alf) in the singular, (miʾatān and alfān) in the dual, (for both), that is, for the masculine and the feminine, with nothing to distinguish between them."},
    {"type": "matn",
     "ar": "(ثم) تقول فيما زاد على «مائة وألف» وما يتفرع عنهما (بالعطف) أي: بعطف الزائد عليهما، أو عطفهما على الزائد",
     "en": "(Then) you say, for what exceeds “a hundred and a thousand” and what branches off from them, (by conjunction), that is, by conjoining the excess to them, or conjoining them to the excess,"},
    {"type": "matn",
     "ar": "حال كون الزائد واقعا (على) صورة (ما تقدم) من أسماء الأعداد من غير تغيير وتبديل،",
     "en": "the excess occurring (in) the form (of what preceded) among the number nouns, without alteration or change."},
    {"type": "matn",
     "ar": "فتقول: «مائة، وواحد، أو واحدة»[[٣]]، و«مائة واثنان، أو اثنتان»، و«مائة وثلاثة رجال، أو ثلاث نسوة»،",
     "en": "So you say: “miʾa wa-wāḥid, or wāḥida” (a hundred and one), “miʾa wa-ithnān, or ithnatān” (a hundred and two), “miʾa wa-thalāthat rijāl, or thalāth niswa” (a hundred and three men, or three women),"},
    {"type": "matn",
     "ar": "و«مائة وأحد عشر رجلا، أو إحدى عشرة امرأة»، و«مائة وأحد وعشرون رجلا، أو إحدى وعشرون امرأة»،",
     "en": "“miʾa wa-aḥada ʿashara rajulan, or iḥdā ʿashrata imraʾatan” (a hundred and eleven men, or women), “miʾa wa-aḥad wa-ʿishrūna rajulan, or iḥdā wa-ʿishrūna imraʾatan” (a hundred and twenty-one men, or women),"},
    {"type": "matn",
     "ar": "و«مائة واثنان وعشرون رجلا، أو اثنتان وعشرون امرأة» و«مائة وثلاثة وعشرون رجلا،",
     "en": "“miʾa wa-ithnān wa-ʿishrūna rajulan, or ithnatān wa-ʿishrūna imraʾatan” (a hundred and twenty-two men, or women), and “miʾa wa-thalātha wa-ʿishrūna rajulan,…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 427 (its note ٤) ----------------
    # Continues «...بل أجملها ليحمل» at the foot of PDF p. 427.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "العطف في قوله: ثم بالعطف على ما تقدم على العطف المطلق الأعم من عطف الأكثر على الأقل والعكس",
     "en": "…the conjunction in his words “then by conjunction in [the form of] what preceded” as conjunction without qualification, more general than conjoining the greater to the lesser and the reverse."},
    {"type": "pair",
     "ar": "هذا على طبق ما ذكره الشارح متابعة لما في الحواشي الهندية،",
     "en": "This accords with what the commentator stated, following what is in the Indian glosses (al-Ḥawāshī al-Hindiyya);"},
    {"type": "pair",
     "ar": "أما على ما ذكره الرضي من أن عطف الأقل على الأكثر جائز في الكل، والعكس أكثر، فلا يتم هذه النكتة.",
     "en": "but on what al-Raḍī stated, namely that conjoining the lesser to the greater is permissible in all cases and the reverse is more frequent, this subtle point does not hold."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خص العطف منها بعطف العقود على الزائد مع أن عطف الزائد على العقود أيضا جائز،",
     "en": "He restricted the conjunction among them to conjoining the decades to the excess, although conjoining the excess to the decades is also permissible,"},
    {"type": "pair",
     "ar": "وإن كان الأول أكثر استعمالا بقرينة قوله: إلى تسعة وتسعين بخلاف قوله: ثم بالعطف على ما تقدم حيث جعله شاملا لهما كما هو الظاهر.",
     "en": "even if the former is more frequent in usage, as indicated by his words “up to ninety-nine”; unlike his words “then by conjunction in [the form of] what preceded”, which he made cover both, as is apparent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل الجار والمجرور حالا من الزائد، لا من الزائد، والعقود معا كما في الرضي؛",
     "en": "He made the preposition and its object a ḥāl (circumstantial qualifier) of the excess, not of the excess and the decades together, as in al-Raḍī,"},
    {"type": "pair",
     "ar": "لأن الاحتياج إلى التقييد فيما وقع فيه التغيير، وهو الزائد لا في العقود.",
     "en": "because the need for the qualification is in what undergoes alteration, and that is the excess, not the decades."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قوله: أو واحدة عطف على قوله: واحد، وقوله: ومائة واثنان واثنتان عطف على قوله: مائة وواحد",
     "en": "His words “or wāḥida” are conjoined to his words “wāḥid”, and his words “and miʾa wa-ithnān wa-ithnatān” are conjoined to his words “miʾa wa-wāḥid”."},
    {"type": "pair",
     "ar": "وإياك وأن تجعل قوله: ومائة عطفا على واحدة، وتجعل واحدة ومائة عطفا على مائة وواحد، فيكون تمثيلا لعطف الأقل على الأكثر؛",
     "en": "Beware of making his words “and miʾa” conjoined to “wāḥida”, and making “wāḥida wa-miʾa” conjoined to “miʾa wa-wāḥid”, so that it would be an example of conjoining the lesser to the greater;"},
    {"type": "pair",
     "ar": "لأنه مع أن فيه تفويت المناسبة بين مائة وواحد؛ إذ المناسبة له واحد ومائة يمنعه قوله: فيما بعد، ويجوز أن يعكس العطف في الكل، فتأمل.",
     "en": "for, besides the loss of correspondence with “miʾa wa-wāḥid” (since what corresponds to it is “wāḥid wa-miʾa”), it is ruled out by his words further on: “and the conjunction may be reversed in all cases.” So reflect."},
    {"type": "pair",
     "ar": "وبما نقلناه لك عن الرضي أن عطف الأكثر على الأقل أكثر ما عرفت في قوله: ويجوز أن يعكس العطف في الكل على طبق ما في الحواشي الهندية؛",
     "en": "From what we have related to you from al-Raḍī, that conjoining the greater to the lesser is more frequent, you know what lies in his words “and the conjunction may be reversed in all cases”, in accord with what is in the Indian glosses:"},
    {"type": "pair",
     "ar": "لأنه يوهم أن عطف الأقل على الأكثر أرجح على ما لا يخفى على الذائق دقائق طعوم السياق المعدود في سلك السباق.",
     "en": "it suggests that conjoining the lesser to the greater is preferable, as is not hidden from one who tastes the fine flavours of the context, counted among the ranks of those who excel."},
    {"type": "pair",
     "ar": "واعلم أن أصل مائة مئية كسدرة حذف لامها، فلزمها التاء عوضا عنها كما في عزة وثبة ولامها ياء كما حكى الأخفش ميئا بمعنى مائة،",
     "en": "Know that the origin of miʾa is miʾya, like sidra; its final radical (lām) was elided and the tāʾ became fixed to it as a substitute for it, as in ʿiza and thuba; and its final radical is yāʾ, as al-Akhfash reported miʾy in the sense of miʾa."},
    # REVIEW: «والحق» is printed without hamza; possibly «وألحق»; transcribed as printed.
    {"type": "pair",
     "ar": "وإنما يكتب مائة بالألف بعد الميم حتى لا يشتبه بصورة منه خطأ، والحق التثنية بالمفرد دون الجمع.",
     "en": "Miʾa is written with an alif after the mīm only so that it is not mistakenly confused with the written form of “minhu”; and the dual was attached to the singular [in this], not the plural."},
]
