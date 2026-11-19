# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 586 (printed ٥٨٥)."""

PAGE_NUMBER = 586
PRINTED_PAGE = "٥٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وما كان» at the foot of PDF p. 585 (mid-sentence).
    {"type": "matn",
     "ar": "حصوله مقدرا في الماضي[[١]] كان منتفيا فيه قطعا، فيلزم لأجل انتفائه انتفاء ما علق به[[٢]] أيضا.",
     "en": "…whose occurrence is supposed in the past was certainly non-existent in it; so, because of its non-occurrence, the non-occurrence of what was made dependent on it necessarily follows as well."},
    {"type": "matn",
     "ar": "فإذا قلت مثلا: «لو جئتني لأكرمتك» فقد علقت حصول الإكرام في الماضي بحصول مجيء مقدر فيه،",
     "en": "So if you say, for example, “law jiʾtanī la-akramtuka” (had you come to me, I would have honoured you), you have made the occurrence of honouring in the past dependent on the occurrence of a coming supposed in it;"},
    {"type": "matn",
     "ar": "فيلزم انتفاؤهما معا وكون انتفاء الإكرام مسببا لانتفاء المجيء في زعم المتكلم،",
     "en": "so there follows the non-occurrence of both together, and the non-occurrence of the honouring being caused by the non-occurrence of the coming, in the speaker’s view."},
    {"type": "matn",
     "ar": "واستعمال «لو» بهذا المعنى هو الكثير المتعارف.",
     "en": "The use of “law” in this sense is the frequent and customary one."},
    {"type": "matn",
     "ar": "وقد يستعمل على قصد لزوم الثاني للأول مع انتفاء اللازم، ليستدل به على انتفاء الملزوم",
     "en": "It is sometimes used with the intent of the second being a necessary consequence (luzūm) of the first, together with the non-occurrence of the consequent (al-lāzim), so that this may serve as evidence for the non-occurrence of the antecedent (al-malzūm),"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿لو كان فيهما آلهة إلا الله لفسدتا﴾[[٣]]،",
     "en": "as in His words, the Exalted: “Had there been in them gods other than Allah, they would both have been ruined”;"},
    {"type": "matn",
     "ar": "فإن «لو» ههنا تدل على لزوم الفساد، لتعدد الآلهة، وعلى أن الفساد منتف، فيعلم من ذلك انتفاء التعدد،",
     "en": "for “law” here indicates that ruin necessarily follows from a plurality of gods, and that ruin is absent; and from this the absence of plurality is known."},
    {"type": "matn",
     "ar": "ومن هذا الاستعمال[[٤]] توهم المصنف أن «لو» لانتفاء الأول لانتفاء الثاني، وخطأ عكسه المشهور،",
     "en": "From this use the author imagined that “law” is for the non-occurrence of the first because of the non-occurrence of the second, and judged its well-known converse to be mistaken;"},
    {"type": "matn",
     "ar": "ولم يدر أن ما ذكره معنى يقصد إليه في مقام الاستدلال بانتفاء اللازم المعلوم على انتفاء الملزوم المجهول،",
     "en": "and he did not realize that what he mentioned is a meaning intended in the context of inferring the non-occurrence of an unknown antecedent from the non-occurrence of a known consequent,"},
    # REVIEW: printed «انتفاأين» and «الانتفاأين» (unusual spelling of the dual of «انتفاء»); transcribed as printed.
    {"type": "matn",
     "ar": "وأن المعنى المشهور بيان سببية أحد انتفاأين معلومين للآخر بحسب الواقع، فلا يتصور هناك استدلال،",
     "en": "whereas the well-known meaning is a statement that one of two known non-occurrences is, in fact, the cause of the other, so that no inference can be conceived there."},
    {"type": "matn",
     "ar": "فإنك إذا قلت: «لو جئتني لأكرمتك» لم تقصد أن تعلم المخاطب انتفاء المجيء من انتفاء الإكرام كيف؟",
     "en": "For when you say “law jiʾtanī la-akramtuka”, you do not intend to let the addressee know the non-occurrence of the coming from the non-occurrence of the honouring — how could you?"},
    {"type": "matn",
     "ar": "وكلا الانتفاأين معلوم له بل قصدت إعلامه بأن انتفاء الإكرام مستند إلى انتفاء المجيء.",
     "en": "Both non-occurrences are known to him; rather, you intended to inform him that the non-occurrence of the honouring rests on the non-occurrence of the coming."},
    {"type": "matn",
     "ar": "ولها استعمال ثالث، وهو أن يقصد بيان استمرار شيء، فيربط ذلك الشيء بأبعد النقيضين عنه",
     "en": "It has a third use: when the intent is to state the continuance of something, and that thing is linked to the more remote of the two contradictories from it,"},
    {"type": "matn",
     "ar": "كقولك: «لو أهانني لأكرمته» لبيان استمرار وجود الإكرام،",
     "en": "as in your saying “law ahānanī la-akramtuhu” (had he insulted me, I would have honoured him), to state the continuance of honouring;"},
    {"type": "matn",
     "ar": "فإنه إذا استلزم الإهانة الإكرام فكيف لا يستلزم الإكرام الإكرام؟",
     "en": "for if insult entails honouring, how could honouring not entail honouring?"},
    {"type": "matn",
     "ar": "(وتلزمان) أي: «إن»، و«لو» (الفعل لفظا) كما مر في الأمثلة (أو تقديرا)",
     "en": "(And they require), that is, “in” and “law”, (a verb, either explicitly), as in the examples given, (or by supposition),"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿وإن أحد من المشركين استجارك﴾[[٥]]، و﴿لو أنتم تملكون﴾[[٦]]، أي: «وإن",
     "en": "as in His words, the Exalted: “And if one of the polytheists seeks your protection” and “If you possessed”, that is, “and if…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أن التقدير لا ينافي الوجود، بل يعم الموجود والمعدوم كما حقق في محله.",
     "en": "Against this: supposition does not exclude existence; rather, it covers both the existent and the non-existent, as has been established in its proper place."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا إذا استلزم انتفاء الملزوم انتفاء اللازم، أو يكون سببا له وكلاهما ممنوعان.",
     "en": "This holds only if the non-occurrence of the antecedent entails the non-occurrence of the consequent, or is a cause of it; and both of these are contested."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الأنبياء: ٢٢.",
     "en": "Qurʾān, Sūrat al-Anbiyāʾ 21:22."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قد صرح المصنف سبب تخطئتهم فقال: الشرط سبب، والجزاء مسبب، والمسبب قد يكون أعم من السبب، فلا يلزم من انتفاء السبب انتفاؤه.",
     "en": "The author stated explicitly his reason for judging them mistaken, saying: the condition (al-sharṭ) is a cause, and the apodosis (al-jazāʾ) is an effect, and the effect may be more general than the cause, so its non-occurrence does not follow from the non-occurrence of the cause."},
    {"type": "pair",
     "ar": "ووافقه الرضي في الدعوى، وزيف الدليل بأن الشرط لا ينحصر في السبب.",
     "en": "Al-Raḍī agreed with him in the claim but rejected the proof, on the grounds that the condition is not restricted to the cause."},
    {"type": "pair",
     "ar": "واستدل على دعواه بأن الشرط ملزوم، والجزاء لازم، واللازم قد يكون أعم، فلا يلزم من انتفائه انتفاؤه.",
     "en": "He argued for his claim instead that the condition is an antecedent (malzūm) and the apodosis a consequent (lāzim), and the consequent may be more general, so the non-occurrence of the latter does not follow from the non-occurrence of the former."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة التوبة: ٦.",
     "en": "Qurʾān, Sūrat al-Tawba 9:6."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة الإسراء: ١٠٠.",
     "en": "Qurʾān, Sūrat al-Isrāʾ 17:100."},
]
