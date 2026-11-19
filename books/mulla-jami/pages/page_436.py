# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 436 (printed ٤٣٥)."""

PAGE_NUMBER = 436
PRINTED_PAGE = "٤٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… وتعريف المؤنث وجودي.» at the foot of PDF p. 435 (new sentence).
    {"type": "matn",
     "ar": "(المؤنث: ما فيه[[١]]) أي: اسم كان فيه (علامة التأنيث لفظا) أي: ملفوظة كانت تلك العلامة حقيقة كـ«امرأة وناقة وغرفة» أو حكما[[٢]] كـ«عقرب»؛",
     "en": "(The feminine is that in which there is), that is, a noun in which there is, (a mark of the feminine, in wording), that is, pronounced, that mark being so either really, as in “imraʾa” (woman), “nāqa” (she-camel) and “ghurfa” (room), or by legal status (ḥukman), as in “ʿaqrab” (scorpion);"},
    {"type": "matn",
     "ar": "إذ الحرف الرابع في المؤنث السماعي في حكم تاء التأنيث، ولهذا لا يظهر التاء في تصغير الرباعي من المؤنثات السماعية",
     "en": "for the fourth letter in a feminine known by attested usage (samāʿī) has the status of the feminine tāʾ; for this reason the tāʾ does not appear in the diminutive of the quadriliteral among the feminines known by attested usage,"},
    {"type": "matn",
     "ar": "(أو تقديرا) أي: مقدرة غير ظاهرة في اللفظ كـ«دار ونار ونعل وقدم» وغيرها من المؤنثات السماعية.",
     "en": "(or by supposition), that is, supposed and not apparent in the wording, as in “dār” (house), “nār” (fire), “naʿl” (sandal) and “qadam” (foot), and other feminines known by attested usage."},
    {"type": "matn",
     "ar": "(والمذكر بخلافه) أي: اسم متلبس بمخالفة المؤنث، أي: لم يوجد علامة التأنيث، لا لفظا ولا تقديرا.",
     "en": "(And the masculine is the opposite of it), that is, a noun characterized by differing from the feminine, that is, in which no mark of the feminine is found, neither in wording nor by supposition."},
    {"type": "matn",
     "ar": "(وعلامته) أي: علامة التأنيث (التاء[[٣]] والألف) حال كونها (مقصورة) كـ«سلمى وحبلى» (أو ممدودة) كـ«صحراء وحمراء»،",
     "en": "(And its mark), that is, the mark of the feminine, (is the tāʾ and the alif), whether (shortened) (maqṣūra), as in “Salmā” and “ḥublā” (pregnant), (or lengthened) (mamdūda), as in “ṣaḥrāʾ” (desert) and “ḥamrāʾ” (red)."},
    {"type": "matn",
     "ar": "وقد زاد بعضهم الياء في قولهم: «ذي وتي»، وزعم أنها للتأنيث،",
     "en": "Some have added the yāʾ, in their saying “dhī” and “tī”, and claimed that it is for the feminine;"},
    {"type": "matn",
     "ar": "وليس ذلك بحجة، لجواز أن يكون صيغة موضوعة للمؤنث مثل: «هي وأنت».",
     "en": "but that is no proof, since it may be a form coined for the feminine, like “hiya” and “anti”."},
    {"type": "matn",
     "ar": "(وهو) أي: المؤنث (حقيقي ولفظي).",
     "en": "(And it), that is, the feminine, (is real (ḥaqīqī) and verbal (lafẓī))."},
    {"type": "matn",
     "ar": "(فالحقيقي: ما) أي: اسم (بإزائه) أي: في مقابلته (ذكر من) جنس (الحيوان[[٤]] كـ«امرأة») في مقابلة «رجل» (و«ناقة») في مقابلة «جمل».",
     "en": "(The real is that), that is, a noun, (opposite which), that is, facing which, (is a male of) the genus of (animals, like “imraʾa” (woman)), facing “rajul” (man), (and “nāqa” (she-camel)), facing “jamal” (camel)."},
    {"type": "matn",
     "ar": "(واللفظي: بخلافه) أي: متلبس بمخالفة المؤنث الحقيقي، أي: ليس بإزائه ذكر",
     "en": "(And the verbal is the opposite of it), that is, characterized by differing from the real feminine, that is, there is no male opposite it…"},

    {"type": "rule"},

    # ---------------- Footnote 6 of PDF p. 435, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الاسم جاز تذكيره باعتبار اللفظ، وجاز تأنيثه باعتبار الكلمة،",
     "en": "…of the noun [itself] is intended, it may be made masculine with respect to “the word” (al-lafẓ) and feminine with respect to “the word” (al-kalima)."},
    {"type": "pair",
     "ar": "وكذا الفعل والحرف وحروف الهجاء يجوز فيها الوجهان بالاعتبارين.",
     "en": "Likewise the verb, the particle and the letters of the alphabet: both ways are allowed in them, under the two considerations."},
    {"type": "pair",
     "ar": "وزعم الفراء أن تذكيرها لا يجوز إلا في الشعر، كذا في شرح التسهيل.",
     "en": "Al-Farrāʾ claimed that making them masculine is allowed only in poetry; so it is in Sharḥ al-Tashīl."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يخرج عن تعريف المؤنث المؤنثات الصيغية كهندي، وتا والتي وأنت، وتدخل في تعريف المذكر،",
     "en": "The feminines by form (al-muʾannathāt al-ṣīghiyya), like “hindī”, “tā”, “allatī” and “anti”, fall outside the definition of the feminine and enter the definition of the masculine;"},
    {"type": "pair",
     "ar": "ولو خص التعريف بالمؤنث بالعلامة وما يقابله لقصر مسافة بيان الأحكام؛",
     "en": "and even if the definition was restricted to the feminine by a mark, and what is opposite it, in order to shorten the course of setting out the rules, [this is open to objection,]"},
    {"type": "pair",
     "ar": "لأنها تصير مخصصة بالمؤنثات بالعلامة مع عدم اختصاصها، ولزوم إطلاق المذكر على هذه الصيغ.",
     "en": "because the rules would become specific to the feminines by a mark although they are not specific [to them], and because it entails that “masculine” is applied to these forms."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والحقيقي المقدر العلامة كزينب وسعاد، وغير الحقيقي نار ودار.",
     "en": "The real [feminine] with a supposed mark is like Zaynab and Suʿād; the non-real is “nār” and “dār”."},
    {"type": "pair",
     "ar": "ودليل كون التاء مقدرة والألف رجوعها في التصغير.",
     "en": "The proof that the tāʾ is supposed, and the alif [too], is their return in the diminutive."},
    {"type": "pair",
     "ar": "وأما الزائد على الثلاثي، فحكموا فيه أيضا بتقدير التاء قياسا على الثلاثي؛ إذ هو الأصل،",
     "en": "As for what exceeds the triliteral, they ruled for it too that the tāʾ is supposed, by analogy with the triliteral, since that is the base;"},
    {"type": "pair",
     "ar": "وقد ترجع فيه أيضا شاذا نحو: قديديمة ووريئة في تصغير قدام ووراء كذا في رضي الكافية.",
     "en": "and in it too [the tāʾ] sometimes returns irregularly, as in “qudaydima” and “wurayʾa” in the diminutive of “quddām” (front) and “warāʾ” (behind); so it is in al-Raḍī’s [commentary on] al-Kāfiya."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإن لم يكن بمعنى التأنيث، فإنها تأتي لأربعة عشر معنى، فصلها وحققها الرضي في هذا المقام.",
     "en": "Even if it is not in the sense of the feminine, for it comes for fourteen meanings, which al-Raḍī set out in detail and verified in this place."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "احترز بقوله: من جنس الحيوان عن النخلة، فإنها بإزائها ذكر، فإنه يوصف النخلة بالأنثى والذكر، وليس تأنيثهما بحقيقي.",
     "en": "By his words “of the genus of animals” he excludes the palm tree (al-nakhla), for there is a male opposite it, since the palm is described as female and male, yet the feminine of these two is not real."},
]
