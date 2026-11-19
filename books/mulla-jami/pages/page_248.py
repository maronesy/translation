# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 248 (printed ٢٤٧)."""

PAGE_NUMBER = 248
PRINTED_PAGE = "٢٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(فإن كان) أي: وجد[[١]] (الفعل) أي: ما يدل على الحدث، فيعم الفعل، واسمي الفاعل والمفعول والصفة المشبهة وغيرها",
     "en": "(If there is), that is, if there exists, (the verb), that is, what denotes the event, so that it includes the verb, the active and passive participles, the resembling adjective (al-ṣifa al-mushabbaha) and others,"},
    {"type": "matn",
     "ar": "(لفظا وجاز) أي: لم يجب (العطف) ولم يمتنع،",
     "en": "(in wording, and conjunction (ʿaṭf) is permissible), that is, it is neither required nor barred,"},
    {"type": "matn",
     "ar": "فلا ينتقض بمثل: «ضربت زيدا وعمرا» لوجوب العطف[[٢]] فيه",
     "en": "so [the rule] is not breached by such a case as “I struck Zayd and ʿAmr,” because conjunction is required in it,"},
    {"type": "matn",
     "ar": "(فالوجهان[[٣]]) أي: العطف والنصب على المفعولية جائزان (نحو: «جئت أنا وزيدا») بالنصب على المفعولية",
     "en": "(then the two options), that is, conjunction and the accusative as object, are both permissible, (as in “I came, I, along with Zayd (wa-Zaydan)”) with the accusative as object,"},
    # REVIEW: the second example is printed «زيدا» (with tanwīn fatḥ), though described as nominative by conjunction (expected «زيد»); transcribed as printed.
    {"type": "matn",
     "ar": "(و«زيدا») بالرفع على العطف.",
     "en": "(and “Zayd”) with the nominative by conjunction."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يجز العطف بل يمتنع (تعين النصب[[٤]] مثل: «جئت وزيدا»)",
     "en": "(Otherwise), that is, if conjunction is not permissible but barred, (the accusative is determinate, as in “I came along with Zayd”);"},
    {"type": "matn",
     "ar": "فإن العطف فيه ممتنع[[٥]]، لعدم الفاصلة، لا بتأكيد المتصل بالمنفصل ولا بغيره.",
     "en": "for conjunction in it is barred, there being no separation, neither by corroborating the attached pronoun with a detached one nor by anything else."},
    {"type": "matn",
     "ar": "(وإن كان الفعل معنى) أي: أمرا معنويا مستنبطا من اللفظ (وجاز) أي: لم يمتنع (العطف تعين العطف[[٦]])",
     "en": "(And if the verb is in meaning), that is, a notional matter inferred from the wording, (and conjunction is permissible), that is, not barred, (conjunction is determinate),"},
    {"type": "matn",
     "ar": "حيث لا يحمل على عمل العامل المعنوي بلا حاجة[[٧]]، مع جواز وجه آخر، وهو العطف",
     "en": "since [the noun] is not made to bear the action of a notional governor without need, when another option, namely conjunction, is permissible,"},
    {"type": "matn",
     "ar": "(نحو: «ما لزيد وعمرو؟»",
     "en": "(as in “What is with Zayd and ʿAmr?”)."},
    {"type": "matn",
     "ar": "وإلا[[٨]]) أي: وإن لم يجز العطف بل امتنع (تعين النصب) حيث لا وجه سواه",
     "en": "(Otherwise), that is, if conjunction is not permissible but barred, (the accusative is determinate), there being no other option,"},
    {"type": "matn",
     "ar": "(نحو: «ما لك وزيدا؟» و«ما شأنك وعمرا؟») فإنه امتنع العطف فيهما؛ لأن العطف على الضمير المجرور[[٩]] بلا إعادة",
     "en": "(as in “What is with you and Zayd?” and “What is your business with ʿAmr?”); for conjunction is barred in both, because conjunction with a genitive pronoun without repeating…"},

    {"type": "rule"},

    # Continuation of footnote ٩ from PDF p. 247.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "جاز تقديم المعطوف على عامله إذا تأخر عن المعطوف عليه.",
     "en": "…it is permissible to place the conjoined noun before its governor if it comes after the noun to which it is conjoined."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "جعل كان تامة، فقوله: لفظا تمييز أو حال.",
     "en": "He made “kāna” complete (tāmma), so his word “in wording” is a specification (tamyīz) or a circumstantial accusative (ḥāl)."},
    {"type": "pair",
     "ar": "ويحتمل أن تكون ناقصة. والأول أولى، تأمل تعرف.",
     "en": "It may also be incomplete (nāqiṣa). The first is preferable; reflect and you will know."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما وجب العطف فيه؛ لأن الأصل في هذه الواو العطف.",
     "en": "Conjunction is required in it only because the base of this wāw is conjunction."},
    {"type": "pair",
     "ar": "وإنما يعدل عنه نصا على المراد من المصاحبة.",
     "en": "One departs from it only to state explicitly that accompaniment is meant."},
    {"type": "pair",
     "ar": "وفي المثال المفروض لا يمكن التنصيص بالنصب على المصاحبة لكون النصب في العطف الذي هو الأصل أظهر.",
     "en": "In the supposed example it is not possible to state accompaniment explicitly by the accusative, because the accusative under conjunction, which is the base, is more evident."},
    {"type": "pair",
     "ar": "إن قلت: فإن عمرا في المثال المذكور ليس مفعولا معه، وكلامنا فيه، فلا حاجة إلى قوله: لم يجب ليخرج؟",
     "en": "If you say: “ʿAmr” in the example mentioned is not an object of accompaniment, and our discussion concerns that; so there is no need for his words “not required” in order to exclude it?"},
    {"type": "pair",
     "ar": "قلنا: كان الكلام هنا لا يختص به، وإلا لم يقل بعد ذلك تعين العطف.",
     "en": "We say: the discussion here is not restricted to it; otherwise he would not have said afterwards “conjunction is determinate.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جعله مفعولا معه ومعطوفا لا العطف وعدمه حتى يتحد الشرط والجزاء.",
     "en": "That is, making it an object of accompaniment or a conjoined noun, not conjunction and its absence, so that the condition and the consequent [would be] one."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ذهب غير المصنف إلى ترجيحه.",
     "en": "Others than the author held it to be preferred."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ذهب الجمهور إلى أن العطف في الصورة المذكورة قبيح. ولهذا قالوا فيها: إن النصب مختار.",
     "en": "The majority held that conjunction in the case mentioned is ugly; for this reason they said of it that the accusative is preferred."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "عند غير المصنف ترجح العطف.",
     "en": "According to others than the author, conjunction is preferred."},
    {"type": "pair",
     "ar": "فإن قلت: ما لزيد وعمرو خارج عن التقسيم؛ لأنه ليس مفعولا معه، بل من التوابع؟",
     "en": "If you say: “What is with Zayd and ʿAmr?” falls outside the division, because it is not an object of accompaniment but one of the appositives (tawābiʿ)?"},
    {"type": "pair",
     "ar": "قلت: هو مفعول معه إذا صرح بمعنى الفعل، فيقال: ما يصنع زيد وعمرو؟",
     "en": "I say: it is an object of accompaniment if the meaning of the verb is made explicit, so that one says: “What are Zayd and ʿAmr doing?”"},
    {"type": "pair",
     "ar": "والمراد بالمفعول معه المذكور بعد الواو لمصاحبة غير المفعول به سواء كان مفعولا معه ظاهرا أو حقيقة، فافهم.",
     "en": "What is meant by the object of accompaniment is what is mentioned after the wāw for accompanying something other than the direct object, whether it is an object of accompaniment outwardly or in reality. So understand."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الحاجة ثابتة فيه، وهي التنصيص على المصاحبة.",
     "en": "Shaykh al-Raḍī said: the need is present in it, namely stating accompaniment explicitly."},
    {"type": "pair",
     "ar": "ولهذا جوز القوم النصب مع اختيار العطف.",
     "en": "For this reason the scholars allowed the accusative while preferring conjunction."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأولى أن يقال: إن قصد النص على المصاحبة وجب النصب، وإلا فلا.",
     "en": "It is better to say: if explicit statement of accompaniment is intended, the accusative is required; otherwise not."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الكوفيون يجوزونه في السعة، والبصريون للضرورة.",
     "en": "Shaykh al-Raḍī said: the Kūfans allow it in ordinary usage, and the Baṣrans [only] under [metrical] necessity."},
    {"type": "pair",
     "ar": "وأما في السعة فيجوزونه بتكلف. وذلك بإضمار حرف الجر مع أنه لا يعمل مقدرا لضعفه.",
     "en": "As for ordinary usage, they allow it with strain, by supposing a suppressed preposition, although it does not govern when implied, because of its weakness."},
    {"type": "pair",
     "ar": "قال الأندلسي: يجوز العطف على ضعف إن لم يقصد النص على المصاحبة،",
     "en": "Al-Andalusī said: conjunction is permissible, though weak, if explicit statement of accompaniment is not intended;"},
    {"type": "pair",
     "ar": "وهو أولى مما قاله المصنف لوروده في القرآن كقوله تعالى: ﴿تساءلون به والأرحام﴾ (سورة النساء: ١)، بالجر في قراءة حمزة.",
     "en": "and this is preferable to what the author said, because it occurs in the Qurʾān, as in His words, the Exalted: “through whom you ask one another, and the wombs” (Qurʾān, Sūrat al-Nisāʾ 4:1), with the genitive in the reading of Ḥamza."},
]
