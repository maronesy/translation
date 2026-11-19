# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 63 (printed ٦٢)."""

PAGE_NUMBER = 63
PRINTED_PAGE = "٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "والأول: إما أن يشبه مبني الأصل أو لا، وهذا أعني: المركب الذي لم يشبه مبني الأصل، هو المعرب، وما عداه أعني: غير المركب، والمركب الذي يشبه مبني الأصل مبني.",
     "en": "As for the first [division]: it either resembles that which is indeclinable in its very origin (mabniyy al-aṣl), or it does not. This — I mean the compound (murakkab) that does not resemble what is indeclinable in origin — is the declinable (muʿrab); while what is other than it — I mean the non-compound, together with the compound that does resemble what is indeclinable in origin — is indeclinable (mabnī)."},

    {"type": "matn",
     "ar": "(فالمعرب[[١]]) الذي هو قسم من الاسم[[٢]] (المركب) أي: الاسم الذي ركب مع غيره تركيبا يتحقق معه عامله.",
     "en": "“So the declinable (fa-l-muʿrab)” — which is one of the divisions of the noun — “the compound (al-murakkab)”: that is, the noun that has been combined with something else in a composition alongside which its governing agent (ʿāmil) is realized."},

    {"type": "matn",
     "ar": "فيدخل فيه «زيد، وقائم، وهؤلاء» في قولك: «زيد قائم»، و«قام هؤلاء»، بخلاف ما ليس بمركب أصلا من الأسماء المعدودة نحو: «ألف، با، تا، زيد، عمرو، بكر»، وبخلاف ما هو مركب مع غيره، لكن لا تركيبا يتحقق معه عامله[[٣]]، ك«غلام» في «غلام زيد»[[٤]]، فإن جميع ذلك من قبيل المبنيات عند المصنف.",
     "en": "Thus there enter under it “Zaydun,” “qāʾimun,” and “hāʾulāʾi” in your saying “Zaydun qāʾimun” (Zayd is standing) and “qāma hāʾulāʾi” (these stood), as opposed to what is not a compound at all — among the enumerated nouns (al-asmāʾ al-maʿdūda) — such as: alif, bā, tā, Zayd, ʿAmr, Bakr; and as opposed to what is compounded with something else, yet not in a composition alongside which its governing agent is realized, like “ghulām” in “ghulāmu Zaydin” (Zayd’s servant); for all of that is, in the author’s view, of the category of the indeclinables (mabniyyāt)."},

    {"type": "matn",
     "ar": "(الذي لم يشبه) أي: لم يناسب[[٥]] مناسبة مؤثرة في منع الإعراب[[٦]] (مبني الأصل) أي: مبني الذي هو الأصل في البناء[[٧]]، فالإضافة بيانية، وهو[[٨]]:",
     "en": "“Which does not resemble (alladhī lam yushbih)” — that is, does not bear a resemblance that is effective in barring inflection — “that which is indeclinable in origin (mabniyy al-aṣl)”: that is, the indeclinable that is the very foundation (aṣl) of indeclinability; so the genitive construction is explicative (bayāniyya). And it [i.e., what is indeclinable in origin] is:"},

    {"type": "matn",
     "ar": "١- الماضي.",
     "en": "1 — the past-tense verb (al-māḍī)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الفاء للتفسير، والمصحح لدخول الفاء الموضوعة للتعقيب على المفسر كون ذكر ذلك المفسر بعد ذكر المفسر.",
     "en": "The fāʾ [in fa-l-muʿrab] is for explication. What validates the entry of the fāʾ — which is [ordinarily] posited to express immediate sequence (taʿqīb) — upon the explanatory clause is that the explicated matter is mentioned after the mention of that which explains it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن اللام الداخلة على هذا الاسم للعهد، والإشارة إلى القسم الذي هو الاسم المعرب. وذلك لأنه ذاكر أحوال الاسم وأقسامه.",
     "en": "He means: the lām attached to this noun [al-muʿrab] denotes definite reference (al-ʿahd), pointing to the division which is the declinable noun. That is because he is [in the course of] mentioning the states of the noun and its divisions."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أعم من أن يكون ذلك العامل لفظيا، أو معنويا مذكورا، أو محذوفا، فالمقارنة المفهومة من لفظ «مع» هي المقارنة بحسب المعنى.",
     "en": "[This is] more general than that the governing agent be verbal (lafẓī), or notional (maʿnawī), whether mentioned or elided; for the concomitance understood from the word “with” (maʿa) is concomitance in respect of meaning."},
    {"type": "pair",
     "ar": "ثم لا يخفى أن اعتبار هذا القيد بعيد؛ إذ لا قرينة في العبارة تدل عليه. وأيضا اعتبار العامل في تعريف المعرب يستلزم الدور، فإن الإعراب معتبر في تعريف العامل، والمعرب معتبر في تعريف الإعراب، فلو كان العامل معتبرا في تعريف المعرب يلزم الدور كما لا يخفى.",
     "en": "Then it is not hidden that taking this restriction into account is far-fetched, since there is no contextual indicator in the wording that points to it. Moreover, taking the governing agent into account in the definition of muʿrab entails circularity (dawr), for inflection (iʿrāb) is taken into account in the definition of the governing agent, and muʿrab is taken into account in the definition of iʿrāb; so were the governing agent taken into account in the definition of muʿrab, circularity would result, as is not hidden."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الغلام بسكون الميم؛ لأنه كسائر الأسماء المعدودة.",
     "en": "“Ghulām” is [here pronounced] with a sukūn on the mīm, because it is like the rest of the enumerated nouns."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فسر الإشباه الذي هو المشاركة في الكيفية بالمناسبة التي هي أعم منه؛ لأن المصنف فسره بذلك. وذلك لأن مانع الإعراب هو الثاني لا خصوصية الأول. ولذا قال: المبني ما ناسب.",
     "en": "He interpreted “resemblance” (al-ishbāh) — which is a sharing in quality (kayfiyya) — by “correspondence” (al-munāsaba), which is more general than it, because the author interpreted it thus. That is because the barrier to inflection is the second [i.e., correspondence], not the specific character of the first. For this reason he said: “the indeclinable is that which corresponds.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "مبنية في بحث المبني، فلا يلزم في التعريف جهالة كما يلزم إذا فسر المناسبة بالمناسبة التي لها قوة ولم يبين، فإن للقوة عرضا واسعا، وليس بعمومه مرادا.",
     "en": "It is grounded in the discussion of the indeclinable (al-mabnī), so no obscurity (jahāla) results in the definition — unlike what results were “correspondence” interpreted as the correspondence that possesses a [certain] force (quwwa) without his specifying it; for “force” has a wide extension, and its full generality is not what is intended."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يفسر مبني الأصل لأنه بهذا المعنى لا ينحصر في الثلاثة؛ لأن أصل جميع الأفعال البناء، وإنما الإعراب فيها لعارض المشابهة بالاسم، ولأن فيه صرف العبارة عن الظاهر؛ لأن المتبادر من مبني الأصل أنه مبني، وذلك بحسب الأصالة دون العروض.",
     "en": "He did not [directly] interpret “indeclinable in origin,” because in this sense it is not confined to the three [categories]; for the origin of all verbs is indeclinability, inflection accruing to them only through the accidental resemblance to the noun. Also because [such an interpretation] would involve diverting the wording from its apparent sense, for what first comes to mind from “indeclinable in origin” is that it is indeclinable — and that by way of original status (aṣāla), not by way of accident (ʿuruḍ)."},
    {"type": "pair",
     "ar": "والمتبادر مما يصدق عليه البناء أن أصله أن يبنى سواء بني كما في أصله، أو عرض له الإعراب.",
     "en": "And what first comes to mind regarding that to which “indeclinability” truly applies is that its origin is to be built (indeclinable) — whether it is [actually] built, as in its origin, or inflection has accidentally accrued to it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: المبني الأصل ثلاثة.",
     "en": "That is: the [categories] indeclinable in origin are three."},
]
