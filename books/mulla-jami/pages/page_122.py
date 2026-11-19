# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 122 (printed ١٢١)."""

PAGE_NUMBER = 122
PRINTED_PAGE = "١٢١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "كما في «ثلاث وأحمر».",
     "en": "…as in “thulāth” [for deviation] and “aḥmar” [for the verbal pattern]."},
    {"type": "matn",
     "ar": "(وهما) أي: العدل ووزن الفعل (متضادان[[١]])؛ لأن الأسماء المعدولة بالاستقراء على أوزان مخصوصة[[٢]] ليس شيء منها من أوزان الفعل المعتبرة في منع الصرف (فلا يكون) أي: لا يوجد معها شيء من الأمر الدائر[[٣]] بين مجموع هذين الشيئين وبين أحدهما فقط (إلا أحدهما) فقط لا مجموعهما[[٤]].",
     "en": "(And they) — that is, deviation and the verbal pattern — (are two contraries); because the deviated nouns, by inductive survey, are upon particular patterns, none of which is among the verbal patterns reckoned in denying full inflection. (So there is not) — that is, there is not found together with [proper-nounhood] anything of the alternation ranging between the sum of these two things and merely one of them — (except one of the two) alone, not their sum."},
    {"type": "matn",
     "ar": "(فإذا نكر) غير المنصرف الذي أحد أسبابه العلمية (بقي بلا سبب[[٥]]) أي: لم يبق فيه سبب[[٦]] من حيث هو سبب فيما هي شرط فيه من الأسباب الأربعة المذكورة؛ لأنه قد انتفى أحد السببين الذي هو العلمية بذاتها، والسبب الآخر المشروط بالعلمية من حيث وصف هو سببيته، فلا يبقى فيه سبب من حيث هو سبب.",
     "en": "(So when the imperfectly inflected [noun] one of whose causes is proper-nounhood is made indefinite, it remains with no cause): that is, no cause remains in it, in respect of its being a cause, among the four aforementioned causes in which [proper-nounhood] is a condition; because one of the two causes — namely proper-nounhood itself — has been negated, and [with it] the other cause, which is conditioned by proper-nounhood in respect of the attribute that is its causal efficacy; so no cause remains in it in respect of its being a cause."},
    {"type": "matn",
     "ar": "(أو على سبب واحد) فيما هي ليست بشرط فيه من العدل ووزن الفعل.",
     "en": "(Or upon a single cause) in that in which [proper-nounhood] is not a condition — namely deviation and the verbal pattern."},
    {"type": "matn",
     "ar": "هذا وقد قيل على قوله: «وهما متضادان» أن «اصمت» بكسرتين علما للمفازة من أوزان الفعل مع وجود العدل فيه، فإنه أمر من «صمت يصمت»، وقياسه أن يجيء بضمتين، فلما جاء بكسرتين علم أنه معدول عنه؟ والجواب: أن هذا أمر غير محقق؛",
     "en": "This being so, an objection has been raised against his statement “and they are two contraries”: namely that “iṣmit,” with two kasras, [used] as a proper name for the desert (mafāza), is of the verbal patterns while deviation is [also] present in it; for it is an imperative from “ṣamata yaṣmutu,” and its regular form would come with two ḍammas [“iṣmut”], so when it came with two kasras it was known that it is deviated from it. The answer [is]: that this is a matter not [firmly] established;"},

    {"type": "rule"},

    # ---------------- Continuation of footnote ٦ from the previous page (printed ١٢٠) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "للوصف، وقد زال بالعلمية.",
     "en": "…to the description (waṣf), and it [the description] has already vanished through proper-nounhood."},
    {"type": "pair",
     "ar": "وذهب جماعة إلى عدم انصرافه اعتبارا للعدل الأصلي.",
     "en": "A group [of grammarians] held that it is not fully inflected, in consideration of the original deviation."},
    {"type": "pair",
     "ar": "وإليه مال الشيخ الرضي قائلا: إن العدل أمر لفظي، وهو باق.",
     "en": "To this Shaykh al-Raḍī inclined, saying: deviation is a verbal matter (amr lafẓī), and it remains."},
    {"type": "pair",
     "ar": "وأما أخر وجمع وأخواته أعلاما فغير منصرفة عند سيبويه اعتبارا للعدل الأصلي، ومنصرفة عند الكوفيين.",
     "en": "As for “Ukhar,” “Jumaʿ,” and its sisters [when used] as proper names, they are imperfectly inflected according to Sībawayh, in consideration of the original deviation, but fully inflected according to the Kufans."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "دفع لما يتوهم من أن القاعدة المذكورة منقوضة بكلمات جامعة للعدل والوزن والعلمية. فإن العلمية مؤثرة فيها مع أنها غير منصرفة بعد التنكير.",
     "en": "[This is] a rebuttal of what might be imagined — that the stated rule is contradicted by words that combine deviation, the [verbal] pattern, and proper-nounhood — [words] in which proper-nounhood is operative, even though they are not fully inflected after being made indefinite."},
    {"type": "pair",
     "ar": "وقد يدفع أيضا بأن العلمية غير مؤثرة معهما لاستقلالهما بمنع الصرف قبل ورودها.",
     "en": "It may also be rebutted [by saying] that proper-nounhood is not operative alongside these two, because the two independently deny full inflection prior to the advent of [proper-nounhood]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هي أوزان ثلاث ومثلث وأخر وسحر وأمس عند تميم، وقطام أيضا عندهم.",
     "en": "These are the patterns of “thulāth,” “mathlath,” “ukhar,” “saḥar,” and “ams” according to [the tribe of] Tamīm, and “Qaṭāmi” too according to them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن المستثنى منه ليس سبب المنع مطلقا، لعدم صحة الحكم، ولا السبب الذي هو أحد الأمرين فيها للزوم استثناء الشيء من نفسه، بل مفهوما مرددا بين مجموع السببين وأحدهما، أو مفهوما مساويا له، أعني: ما يجامعه العلمية المؤثرة، ولم يكن مشروطا بها.",
     "en": "He means: the thing excepted from is neither the cause of denial [of inflection] absolutely — since [then] the ruling would not be sound — nor the cause that is one of the two matters therein — for that would entail excepting a thing from itself — but rather a concept alternating between the sum of the two causes and [merely] one of them, or a concept equivalent to it, I mean: that which operative proper-nounhood coincides with, without being conditioned by it."},
    {"type": "pair",
     "ar": "وهذا المعنى وإن كان منحصرا في أحدهما، لكنه أعم منه بحسب التصور.",
     "en": "And this sense, even though it is confined to one of the two [in reality], is nonetheless more general than it by way of conception (taṣawwur)."},
    {"type": "pair",
     "ar": "وهذا القدر كاف في صحة الاستثناء، كما يقال في كلمة التوحيد.",
     "en": "This much suffices for the soundness of the exception, as is said regarding the formula of divine oneness (kalimat al-tawḥīd)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا حاجة بعد القصر بالنفي والاستثناء إلى قوله: «فقط»، ولا إلى قوله: «لا مجموعهما» كما بين في محله.",
     "en": "After the restriction by negation and exception, there is no need for his phrase “only” (faqaṭ), nor for his phrase “not their sum,” as has been shown in its [proper] place."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: إن كان معها غير واحد منهما.",
     "en": "That is: if there is together with [proper-nounhood] not just one of the two [causes]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وإن كانت الأربعة مجتمعة كما في آذربيجان.",
     "en": "Even if the four [causes] are combined, as in “Ādharbayjān.”"},
]
