# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 206 (printed ٢٠٥)."""

PAGE_NUMBER = 206
PRINTED_PAGE = "٢٠٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وقيدنا المبني بكونه على ما يرفع به[[١]]؛ لأن توابع المستغاث بالألف لا يجوز فيها الرفع نحو: «يا زيداه وعمرا» لا «وعمرو»؛ لأن المتبوع مبني على الفتح.",
     "en": "We restricted the indeclinable to its being [indeclinable] on that by which it is put in the nominative, because the nominative is not allowed in the appositives of the one called for help with the alif, as in “yā Zaydāh wa-ʿAmran,” not “wa-ʿAmrun,” since the antecedent (matbūʿ) is indeclinable on the fatḥa."},
    {"type": "matn",
     "ar": "وقيد التوابع بكونها مفردة؛ لأنها لو لم تكن مفردة لا حقيقة ولا حكما كانت مضافة بالإضافة المعنوية، وحينئذ لا يجوز فيها إلا النصب،",
     "en": "He restricted the appositives to their being single because, were they single neither really nor by status, they would be annexed by semantic annexation, and then only the accusative is allowed in them."},
    {"type": "matn",
     "ar": "وإنما جعلنا المفردة أعم من أن تكون مفردة حقيقة بألا يكون مضافا معنويا ولا لفظيا ولا شبه مضاف أو حكما بأن يكون مضافا لفظيا أو مشابها به،",
     "en": "We made “single” more general than its being really single—in that it is annexed neither semantically nor verbally, nor resembles the annexed—or single by status—in that it is verbally annexed or resembles it—"},
    {"type": "matn",
     "ar": "فإنهما لما انتفت فيهما[[٢]] الإضافة المعنوية كانا في حكم المفرد؛",
     "en": "for since semantic annexation is absent from these two, they have the status of the single—"},
    {"type": "matn",
     "ar": "ليدخل فيها المضافة بالإضافة اللفظية، والمشبهة بالمضاف؛ لأنهما كالتوابع المفردة في جواز الرفع والنصب",
     "en": "so that what is annexed by verbal annexation and what resembles the annexed are included in it; because these two are like the single appositives in allowing the nominative and the accusative,"},
    {"type": "matn",
     "ar": "نحو: «يا زيد الحسن الوجه، والحسن الوجه» و«يا زيد الحسن وجهه[[٣]]، والحسن وجهه».",
     "en": "as in “yā Zaydu al-ḥasanu al-wajhi, wa-l-ḥasana al-wajhi” (O Zayd, the fair of face), and “yā Zaydu al-ḥasanu wajhuhu, wa-l-ḥasana wajhuhu” (O Zayd, whose face is fair)."},
    {"type": "matn",
     "ar": "ولما لم يجز الحكم الآتي في التوابع كلها بل في بعضها، ولم يجز فيما هو جار فيه مطلقا، بل لا بد في بعضها من قيد، فصل التوابع الجاري هذا الحكم فيها.",
     "en": "Since the ruling to come does not apply to all the appositives but to some of them, and does not apply without restriction even where it applies, but some of them need a condition, he specified in detail the appositives to which this ruling applies,"},
    {"type": "matn",
     "ar": "وصرح بالقيد فيما هو محتاج إليه، فقال: (من التأكيد) أي: المعنوي[[٤]]؛",
     "en": "and stated the condition explicitly where it is needed. He said: (among corroboratives—min al-taʾkīd), that is, the semantic [corroborative];"},
    {"type": "matn",
     "ar": "لأن التأكيد اللفظي[[٥]] حكمه في الأغلب حكم الأول إعرابا وبناء، نحو: «يا زيد زيد»[[٦]]، وقد يجوز إعرابه رفعا ونصبا،",
     "en": "because the verbal corroborative (al-taʾkīd al-lafẓī) mostly takes the ruling of the first in declension and indeclinability, as in “yā Zaydu Zaydu,” though its declension in the nominative and the accusative is sometimes allowed;"},
    {"type": "matn",
     "ar": "وكان المختار عند المصنف ذلك، ولذلك لم يقيد التأكيد بالمعنوي",
     "en": "and that was the author’s preferred view; for this reason he did not restrict the corroborative to the semantic one."},
    {"type": "matn",
     "ar": "(والصفة[[٧]]) مطلقا (وعطف البيان[[٨]]) كذلك (والمعطوف) بحرف (الممتنع دخول",
     "en": "(And the qualifier—al-ṣifa) without restriction, (and the explicative apposition—ʿaṭf al-bayān) likewise, (and the [noun] coordinated) by a particle, (for which the entry of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا القيد مستفاد من الحكم، فإن الرفع لا يتصور في تابع المستغاث بالألف.",
     "en": "This condition is derived from the ruling, for the nominative is inconceivable in the appositive of the one called for help with the alif."},
    {"type": "pair",
     "ar": "قيل: وكذا لا يتصور الرفع في توابع العلم الموصوف بـ«ابن» إذا كان مفتوحا.",
     "en": "It has been said: likewise the nominative is inconceivable in the appositives of a proper name qualified by “ibn” when it takes a fatḥa."},
    {"type": "pair",
     "ar": "ولك أن تقول: إن اللام في المبني للعهد إلى ما فهم من قوله: ويبنى على ما يرفع به، فلا حاجة حينئذ إلى التقييد.",
     "en": "You may say that the article in “al-mabnī” refers back to what is understood from his words “and it is made indeclinable on that by which it is put in the nominative,” so there is then no need for the restriction."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فاعتبر حكم المفرد ليتحقق العمل بالشبه بالمفرد كما تحقق العمل بالشبه بالمضاف إذا كانتا منادى.",
     "en": "So the status of the single was taken into account, so that government (ʿamal) is realized through resemblance to the single, just as government is realized through resemblance to the annexed when the two are a munādā."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ويا هؤلاء العشرون رجلا.",
     "en": "And “yā hāʾulāʾi al-ʿishrūna rajulan” (O you, the twenty men)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "صرح في شرح المفصل به.",
     "en": "He stated it explicitly in Sharḥ al-Mufaṣṣal."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وذلك لأن الثاني عين الأول لفظا أو معنى، فكأن حرف النداء باشره كما باشر الأول.",
     "en": "That is because the second is identical to the first in wording or meaning, so it is as though the vocative particle were directly attached to it as it is to the first."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "نص في التأكيد، وفي جعل أبي علي ذلك بدلا، وجعل سيبويه إياه عطف بيان نظر؛ لأنهما يفيدان ما لا يفيده الأول،",
     "en": "It is explicit as a corroborative. Abū ʿAlī’s making it a substitute, and Sībawayh’s making it an explicative apposition, are open to question, because these two convey what the first does not convey."},
    {"type": "pair",
     "ar": "وإذا وصفت الثاني فأبو عمرو يضم الثاني على أنه توكيد لفظي موصوف أو بدل منه لما حصل له من الوصفية",
     "en": "If you qualify the second, Abū ʿAmr gives the second a ḍamma, as a qualified verbal corroborative, or as a substitute for it because of the qualification it has acquired,"},
    {"type": "pair",
     "ar": "كما في قوله تعالى: ﴿بالناصية ناصية كاذبة خاطئة﴾ (سورة العلق: ١٥-١٦)،",
     "en": "as in His words, the Exalted: “by the forelock—a lying, sinful forelock” (Qurʾān, Sūrat al-ʿAlaq 96:15–16);"},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون صفة؛ لأن العلم لا يوصف به.",
     "en": "it cannot be a qualifier, because a proper name is not used as a qualifier."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الأصمعي: لا يوصف المنادى المضموم لشبهه بالمضمر، وارتفاع العالم أو انتصابه في مثل: يا زيد العالم على الاختصاص،",
     "en": "Al-Aṣmaʿī said: the munādā marked with ḍamma is not qualified, because of its resemblance to the pronoun; and the nominative or accusative of “al-ʿālim” in such as “yā Zaydu al-ʿālim” (O Zayd, the learned) is by way of specification (ikhtiṣāṣ)."},
    {"type": "pair",
     "ar": "وفيه أنه لا يلزم من الشبه التساوي في جميع الأحكام.",
     "en": "Against this: resemblance does not entail equality in all rulings."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ذهب الشيخ الرضي إلى أنه بدل، فحكمه حكم البدل عنده.",
     "en": "Shaykh al-Raḍī held that it is a substitute, so its ruling, in his view, is the ruling of the substitute."},
]
