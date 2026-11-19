# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 279 (printed ٢٧٨)."""

PAGE_NUMBER = 279
PRINTED_PAGE = "٢٧٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(أو مقدما) عطف على قوله «بعد إلا»[[١]] أي: المستثنى منصوب وجوبا إذا كان المستثنى مقدما (على المستثنى منه) سواء كان في كلام موجب أو غيره[[٢]]،",
     "en": "(Or placed before) is coordinated with his words “after illā”; that is, the excepted term is necessarily in the accusative when it is placed before (the mustathnā minhu), whether in affirmative speech or otherwise,"},
    {"type": "matn",
     "ar": "نحو: «جاءني إلا زيدا القوم، وما جاءني إلا زيدا أحد» لامتناع تقديم البدل على المبدل منه.",
     "en": "as in “There came to me, except Zayd, the people” and “There did not come to me, except Zayd, anyone,” because a substitute (badal) cannot be placed before that for which it substitutes (al-mubdal minhu)."},
    {"type": "matn",
     "ar": "(أو منقطعا) أي: المستثنى منصوب أيضا وجوبا إذا كان منقطعا بعد «إلا» نحو: «ما في الدار أحد إلا حمارا»",
     "en": "(Or disjoined—munqaṭiʿ), that is, the excepted term is likewise necessarily in the accusative when it is disjoined, after “illā,” as in “There is no one in the house except a donkey,”"},
    {"type": "matn",
     "ar": "(في الأكثر[[٣]]) أي: في أكثر اللغات، وهي لغات أهل الحجاز، فإنهم قبائل كثيرون أو في أكثر مذاهب النحاة، فإن أكثرهم ذهبوا إلى اللغة الحجازية،",
     "en": "(in most [usage]), that is, in most dialects, namely the dialects of the people of the Ḥijāz, for they are many tribes; or in most of the doctrines of the grammarians, for most of them followed the Ḥijāzī usage."},
    {"type": "matn",
     "ar": "فالمنقطع مطلقا منصوب عندهم؛ إذ لا يتصور فيه إلا بدل الغلط، وهو لا يصدر إلا بطريق السهو والغفلة، والمستثنى المنقطع إنما يصدر بطريق الرؤية والفطانة.",
     "en": "So the disjoined [excepted term] is in the accusative absolutely according to them, since only the substitute of error (badal al-ghalaṭ) is conceivable in it, and that arises only through slip and inattention, whereas the disjoined excepted term arises only through deliberation and discernment."},
    {"type": "matn",
     "ar": "وأما بنو تميم، فقد قسموا المنقطع إلى قسمين:",
     "en": "As for the Banū Tamīm, they divided the disjoined [excepted term] into two kinds:"},
    {"type": "matn",
     "ar": "أحدهما: ما يكون قبله اسم يصح حذفه[[٤]]، نحو: «ما جاءني القوم إلا حمارا»، فههنا يجوزون البدل.",
     "en": "The first: that before which there is a noun whose omission is valid, as in “The people did not come to me, except a donkey”; here they allow the substitute."},
    {"type": "matn",
     "ar": "وثانيهما: ما لا يكون قبله اسم يصح حذفه، فهم ههنا يوافقون الحجازيين في إيجاب نصبه،",
     "en": "The second: that before which there is no noun whose omission is valid; here they agree with the Ḥijāzīs in making its accusative necessary,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿لا عاصم اليوم من أمر الله إلا من رحم﴾[[٥]]، أي: من رحمه الله، فمن رحمه الله هو المرحوم المعصوم، فلا يكون داخلا في العاصم، فيكون منقطعا.",
     "en": "as in His words, the Exalted: “There is no protector today from the command of Allah except him on whom He has mercy”; that is, whom Allah has mercy upon. The one on whom Allah has mercy is the one shown mercy and protected, so he is not included in “the protector”; hence it is disjoined."},
    {"type": "matn",
     "ar": "(أو كان بعد «خلا، وعدا») أي: المستثنى منصوب أيضا وجوبا إذا كان بعد «عدا» من «عدا يعدو عدوا» إذا جاوزه مثل: «جاءني القوم عدا زيدا»،",
     "en": "(Or it comes after “khalā” and “ʿadā”), that is, the excepted term is likewise necessarily in the accusative when it comes after “ʿadā,” from “ʿadā yaʿdū ʿadwan,” [said] when one passes beyond something, as in “The people came to me, ʿadā Zayd”;"},
    {"type": "matn",
     "ar": "أو بعد «خلا» من «خلا يخلو خلوا» نحو: «جاءني القوم خلا زيدا»، وهو في الأصل لازم يتعدى إلى المفعول",
     "en": "or after “khalā,” from “khalā yakhlū khuluwwan,” as in “The people came to me, khalā Zayd.” In origin it is intransitive, reaching the object…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا هو الظاهر المنساق إلى الفهم، لكن يتجه أن انتصابه مشروط بكونه بعد \"إلا\". وذلك غير مفهوم من العبارة.",
     "en": "This is the apparent reading that comes first to mind; but an objection arises that its being in the accusative is then conditional on its coming after “illā,” and that is not understood from the wording."},
    {"type": "pair",
     "ar": "وكذا الحال في قوله: أو منقطعا.",
     "en": "The same holds for his words “or disjoined.”"},
    {"type": "pair",
     "ar": "ويمكن أن يجعلا معطوفين على قوله: في كلام موجب حتى لا يتجه ذلك، وهو خبر آخر لـ«كان» أو حال.",
     "en": "The two may be made coordinate with his words “in affirmative speech,” so that this objection does not arise; and that is a second predicate of “kāna” or a circumstantial qualifier (ḥāl)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أشار إلى أن بين هذا القسم وما تقدم تداخلا ولم يقيد كلا منهما بما يقابل به الأخر ليعلم أن ما اجتمع فيه القسمان وجب نصبه لوجهين.",
     "en": "He indicated that this kind and the preceding one overlap, and he did not restrict either of them by what sets it against the other, so that it would be known that where the two kinds coincide the accusative is necessary on two grounds."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "متعلق بمنصوب الملحوظ بطريق الانسحاب أو خبر محذوف.",
     "en": "[It is] connected with “in the accusative,” understood by way of carrying over (insiḥāb), or [it is] the predicate of an elided [subject]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "متعددا كان أو غير متعدد، نحو: ما جاءني زيد إلا عمرا.",
     "en": "Whether it is multiple or not multiple, as in “Zayd did not come to me, except ʿAmr.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة هود: ٤٣.",
     "en": "Qurʾān, Sūrat Hūd 11:43."},
]
