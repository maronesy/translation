# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 61 (printed ٦٠)."""

PAGE_NUMBER = 61
PRINTED_PAGE = "٦٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "٣- (و) منها: دخول (التنوين) بأقسامه، إلا تنوين الترنم، وسيجيء في آخر الكتاب إن شاء الله تعالى تعريفه[[١]]، وبيان أقسامه[[٢]]، على وجه يظهر اختصاص ما عدا تنوين الترنم به[[٣]]، وجهة عدم اختصاص تنوين الترنم به[[٤]].",
     "en": "3 — And among them is the entry of (nunation, tanwīn) in [all] its kinds, except the tanwīn of chanting (tanwīn al-tarannum). Its definition, and the exposition of its kinds, will come at the end of the book — if Allah the Exalted wills — in a manner that will make clear the restriction of all but the tanwīn al-tarannum to it [the noun], and the aspect of the non-restriction of the tanwīn al-tarannum to it."},
    {"type": "matn",
     "ar": "٤- (و) منها: (الإسناد إليه) وهو[[٥]] بالرفع عطف على «دخول»، لا على مدخوله؛ لأن المتبادر من الدخول الذكر في الأول، أو اللحوق بالآخر[[٦]]، وكلاهما منتفيان[[٧]] في الإضافة، وكذا في الإسناد إليه[[٨]]. والمراد[[٩]]: كون الشيء مسندا إليه.",
     "en": "4 — And among them is (predication being made to it, al-isnād ilayhi). It [al-isnād] is in the nominative, conjoined to “the entry (dukhūl),” not to that which the entry governs; because what comes readily to mind from “entry” is [either] mention at the beginning or attachment at the end, and both are absent in annexation (iḍāfa), and likewise in al-isnād ilayhi. What is intended is the thing’s being that to which predication is made."},
    {"type": "matn",
     "ar": "وإنما اختص هذا المعنى بالاسم؛ لأن الفعل وضع[[١٠]] لأن يكون أبدا[[١١]] مسندا فقط، فلو جعل مسندا إليه لزم خلاف وضعه.",
     "en": "This meaning is restricted to the noun only because the verb was coined to be ever a predicate (musnad) alone; so were it made that to which predication is directed (musnad ilayhi), a contravention of its coinage (waḍʿ) would follow."},
    {"type": "matn",
     "ar": "٥- (و) منها: (الإضافة) أي: كون الشيء مضافا، بتقدير حرف الجر لا بذكره[[١٢]] لفظا.",
     "en": "5 — And among them is (annexation, al-iḍāfa), that is, the thing’s being the annexed term (muḍāf), by the implicit supposition (taqdīr) of the genitive particle, not by its explicit mention in wording."},
    {"type": "matn",
     "ar": "ووجه اختصاصها بالاسم: اختصاص لوازمها من التعريف، والتخصيص[[١٣]]،",
     "en": "The aspect of its restriction to the noun is the restriction of its concomitants — [namely] definiteness (taʿrīf), particularization (takhṣīṣ),"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: تعريف التنوين.",
     "en": "That is, the definition of the tanwīn."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وأقسامه خمسة.",
     "en": "And its kinds are five."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بالاسم.",
     "en": "That is, to the noun."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: بالاسم.",
     "en": "That is, to the noun."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: الإسناد إليه.",
     "en": "That is, [the pronoun “it” refers to] al-isnād ilayhi (predication to it)."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: الذكر في الأول، واللحوق في الآخر.",
     "en": "He means: mention at the beginning, and attachment at the end."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: لا يوجدان.",
     "en": "He means: the two of them are not found [present]."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: لأنه أمر معنوي لا لفظي، والدخول واللحوق من عوارض الألفاظ.",
     "en": "That is, because it [predication] is a conceptual matter (amr maʿnawī), not a verbal one (lafẓī), whereas entering and attaching are among the accidents of words."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "يعني: بالإسناد إليه.",
     "en": "He means: [what is intended] by “al-isnād ilayhi.”"},

    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "يعني: أن العرب لاحظت معنى الفعل منساقا إلى أمر مرتبطا به لا غير، بخلاف معنى الاسم، فإنه لاحظته لا على وجه منساق إلى شيء، أو منساقا إلى شيء، فلذا كان صالحا للمتقابلين.",
     "en": "He means: the Arabs regarded the meaning of the verb as directed toward some matter and bound up with it and nothing else; unlike the meaning of the noun, which they regarded either not as directed toward anything, or as directed toward something — and so it was fit for the two opposite [roles, of musnad and musnad ilayhi]."},

    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "منصوب على الظرفية، أي: في الأزمان كلها.",
     "en": "It [abadan, “ever”] is in the accusative as an adverbial of time, that is: in all times."},

    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "بذكر حرف الجر.",
     "en": "[Not] by the explicit mention of the genitive particle."},

    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "المراد بالتخصيص تقليل اشتراك الأفراد. ولا يراد بالفعل إلا الطبيعة، فلا يقبل التخصيص. وفيه تأمل.",
     "en": "What is meant by “particularization” (takhṣīṣ) is the reduction of the sharing among individual instances. And nothing is meant by “the verb” except the nature (ṭabīʿa), so it does not admit of particularization. But this requires reflection."},
    {"type": "pair",
     "ar": "لجواز أن تقول: «ضرب يوم» مريدا به نفس الطبيعة، ولا شبهة في أن هذه الإضافة للتخصيص.",
     "en": "For it is permissible to say “ḍarbu yawmin” (a striking of a day), intending by it the nature itself, and there is no doubt that this annexation is for particularization."},
    {"type": "pair",
     "ar": "ولا يخفى أن هذا النوع من التخصيص جار في الفعل كتخصيصه بالظرف والحال.",
     "en": "It is not hidden that this kind of particularization operates in the verb as well, as in its being particularized by an adverbial (ẓarf) and a circumstantial (ḥāl)."},
    {"type": "pair",
     "ar": "فإن قلت: جريانه فيه باعتبار معناه المصدري، وهو معنى اسمي فلم يوجد إلا في الاسم.",
     "en": "If you say: its operation in [the verb] is by consideration of its verbal-noun meaning (maʿnā maṣdarī), which is a nominal meaning, so it is found only in the noun —"},
    {"type": "pair",
     "ar": "قلنا: المعنى المصدري سواء كان في قالب المصدر أو الفعل صالح لذلك التقييد.",
     "en": "We say: the maṣdar-meaning, whether it be in the mold of the verbal noun or of the verb, is fit for that qualification."},
    {"type": "pair",
     "ar": "وكيف لا؟ والمعنى المصدري المدلول عليه بالفعل مظروف للزمان الذي هو المدلول عليه بالفعل.",
     "en": "And how could it not be, when the maṣdar-meaning signified by the verb is contained within the time that is [also] signified by the verb?"},
    {"type": "pair",
     "ar": "وأيضا لو صح ذلك لم يصح النقض الآتي بـ«مررت بزيد»، فإن الربط المدلول عليه بالباء ليس إلا بين المرور وزيد.",
     "en": "Moreover, were that sound, the forthcoming counter-instance with “marartu bi-Zaydin” (I passed by Zayd) would not hold, for the linkage signified by the bāʾ is nothing but between the passing and Zayd."},
]
