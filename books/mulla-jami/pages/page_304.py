# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 304 (printed ٣٠٣)."""

PAGE_NUMBER = 304
PRINTED_PAGE = "٣٠٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بخلاف «قمت» from the foot of PDF p. 303.
    {"type": "matn",
     "ar": "يوم الجمعة»، فإنه وإن نسب إليه القيام بالحرف المقدر -وهو «في»- لكنه غير مراد؛ إذ لو أريد لانجر به.",
     "en": "…yawma l-jumuʿati” (I stood on Friday): although standing is related to it by a supposed particle, namely “fī,” that particle is not intended, for were it intended, [the noun] would be put in the genitive by it."},
    {"type": "matn",
     "ar": "(فالتقدير) أي: تقدير حرف الجر[[١]].",
     "en": "(So the supposition), that is, the supposition of the preposition,"},
    {"type": "matn",
     "ar": "(شرطه: أن يكون المضاف اسما)؛ إذ لو كان فعلا لا بد من أن يتلفظ بالحرف نحو: «مررت بزيد».",
     "en": "(has as its condition that the annexed word [al-muḍāf] be a noun), for were it a verb, the particle would have to be pronounced, as in “marartu bi-Zaydin.”"},
    {"type": "matn",
     "ar": "(مجردا) أي: منسلخا عنه[[٢]].",
     "en": "(stripped), that is, divested of"},
    {"type": "matn",
     "ar": "(بتنوين) أو ما قام مقامه[[٣]] من نوني التثنية والجمع.",
     "en": "(the tanwīn) or what stands in its place, namely the nūn of the dual and of the [sound] plural,"},
    {"type": "matn",
     "ar": "(لأجلها) أي: لأجل الإضافة؛ لأن التنوين أو النون دليل لتمام ما هي فيه،",
     "en": "(for its sake), that is, for the sake of annexation; for the tanwīn or the nūn is an indication that the word containing it is complete."},
    {"type": "matn",
     "ar": "فلما أرادوا أن يمزجوا الكلمتين مزجا يكتسب به الأولى من الثانية التعريف أو التخصيص أو التخفيف[[٤]]، حذفوا من الأولى علامة تمام الكلمة، وتمموها بالثانية.",
     "en": "So when they wished to blend the two words in a blending by which the first acquires from the second definiteness, specification or lightening, they elided from the first the sign of the word’s completeness and completed it with the second."},
    {"type": "matn",
     "ar": "ثم المتبادر من هذا التعريف[[٥]] -نظرا إلى كلام القوم حيث ليسوا قائلين بتقدير حرف الجر[[٦]] في الإضافة اللفظية- أنه غير شامل للمضاف إليه بالإضافة اللفظية،",
     "en": "What first comes to mind from this definition, in view of the statements of the grammarians, since they do not hold that a preposition is supposed in verbal annexation, is that it does not include the muḍāf ilayhi in verbal annexation (al-iḍāfa al-lafẓiyya);"},
    {"type": "matn",
     "ar": "لكن الظاهر من كلام المصنف في المتن والتصريح في شرحه له أن التقسيم إلى الإضافة",
     "en": "but what is evident from the author’s words in the base text (matn), and what he states explicitly in his commentary on it, is that the division into…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: التقدير المخصوص، وهو تقدير الحرف مرادا، وإلا فالتقدير غير مشروط بهذا الشرط، نحو: «صمت يوم الجمعة، وضربته تأديبا»،",
     "en": "That is, the particular supposition, namely the supposition of the particle as intended; otherwise supposition is not conditioned by this condition, as in “ṣumtu yawma l-jumuʿati” (I fasted on Friday) and “ḍarabtuhu taʾdīban” (I beat him as discipline)."},
    {"type": "pair",
     "ar": "والأولى أن يقول: والإرادة شرطها إلى آخره.",
     "en": "It would have been better for him to say: “and the intending has as its condition…”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أريد بالتجريد الانسلاخ الذي لازم معناه، فلا يرد أن الواجب أن يقول: مجردا عن تنوينه،",
     "en": "That is, by “stripping” (tajrīd) is meant the divesting that is the concomitant of its meaning; so the objection does not arise that he ought to have said “stripped of its tanwīn” [with ʿan]."},
    {"type": "pair",
     "ar": "والأولى أن يجعل من قبيل تضمين معنى الانسلاخ.",
     "en": "It is better to treat it as a case of implication (taḍmīn) of the meaning of divesting."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا في الأكثر، فلا ينتقض بالحسن الوجه؛ لأن الخفة في الإضافة فيه بحذف متعلق المضاف إليه.",
     "en": "This holds in most cases; so it is not contradicted by “al-ḥasanu l-wajhi” (the one handsome of face), for the lightness in its annexation lies in eliding what pertains to the muḍāf ilayhi."},
    {"type": "pair",
     "ar": "ولا ينتقض بكم رجل وحواج بيت الله؛ لأن المراد بحذف التنوين لأجل الإضافة كونه بحيث يجب حذف تنوينه لأجلها لو كان فيه تنوين.",
     "en": "Nor is it contradicted by “kam rajulin” (how many a man) and “ḥawājju bayti llāhi” (the pilgrims to the House of Allah), for what is meant by eliding the tanwīn for the sake of annexation is that the word be such that its tanwīn would have to be elided for its sake, had it a tanwīn."},
    {"type": "pair",
     "ar": "ولا يلزم صحة إضافة الغلام إلى زيد؛ لأن الغلام ليس بحيث لو كان فيه تنوين يسقط بسبب الإضافة، فإنه لو كان فيه تنوين يسقط لأجل اللام.",
     "en": "Nor does it follow that annexing “al-ghulām” to “Zayd” is sound, for “al-ghulām” is not such that, had it a tanwīn, it would drop because of annexation; for had it a tanwīn, it would drop because of the lām [of definition]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كلمة «أو» ههنا لمنع الخلو؛ إذ التخفيف لازم في الكل.",
     "en": "The word “aw” (or) here is for the exclusion of the absence [of all alternatives] (manʿ al-khulūw), since lightening is necessary in every case."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما قال: المتبادر لأنه يمكن تأويل التعريف بأن المراد بواسطة حرف الجر لفظا أو تقديرا أعم من التقدير حقيقة أو حكما.",
     "en": "He said “what first comes to mind” only because the definition can be interpreted to mean that “by means of a preposition, overtly or by supposition” is more general than supposition in reality or by assimilation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ لا معنى لاعتبار حرف في حسن الوجه؛ لأنه هو هو، ولا في ضارب زيد؛ لأنه متعد بنفسه،",
     "en": "For there is no sense in positing a particle in “ḥasanu l-wajhi,” since it [the face] is identical with it [the one handsome], nor in “ḍāribu Zaydin” (the striker of Zayd), since it is transitive by itself."},
    {"type": "pair",
     "ar": "ففي عامل هذا المضاف إليه إشكال؛ إذ ليس هنا حرف جر حتى يعمل فيه.",
     "en": "So there is a difficulty concerning the governor of this muḍāf ilayhi, since there is no preposition here to govern it."},
    {"type": "pair",
     "ar": "ولما لم يكن حرف الجر لم يعمل المضاف ولا الإضافة عمل حرف الجر؛ لأنهما إذا عملا كان ذلك بنيابة حرف الجر.",
     "en": "And since there is no preposition, neither the muḍāf nor the annexation performs the governing of a preposition, for when they govern, it is by standing in for a preposition."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: يجوز أن يقال: عمل المضاف الجر لمشابهة المضاف الحقيقي بتجرده عن التنوين أو النون لأجل الإضافة.",
     "en": "Shaykh al-Raḍī said: it may be said that the muḍāf governs the genitive by its resemblance to the true muḍāf, in being stripped of the tanwīn or the nūn for the sake of annexation."},
]
