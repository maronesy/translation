# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 459 (printed ٤٥٨)."""

PAGE_NUMBER = 459
PRINTED_PAGE = "٤٥٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… مثل اسم الفاعل إذا كان مفردا في العمل. وشروطه:» at the foot of PDF p. 458.
    {"type": "matn",
     "ar": "لعدم تطرق خلل إلى صيغته المفردة من حيث ذاتها بإلحاق علامتي التثنية[[١]] والجمع،",
     "en": "…because no defect reaches its singular form in itself through the addition of the two markers of the dual and the plural;"},
    {"type": "matn",
     "ar": "تقول: «الزيدان ضاربان، أو الزيدون ضاربون عمرا الآن أو غدا»، و«الزيدان الضاربان أو الزيدون الضاربون عمرا الآن أو غدا أو أمس».",
     "en": "you say: “The two Zayds are striking, or the Zayds are striking, ʿAmr now or tomorrow”, and “The two Zayds who are striking, or the Zayds who are striking, ʿAmr now or tomorrow or yesterday”."},
    {"type": "matn",
     "ar": "(ويجوز حذف النون) أي: نون المثنى والمجموع (مع العمل) في معموله بنصبه على المفعولية، بخلاف ما إذا كان مضافا إليه، فإن حذفها واجب",
     "en": "(The omission of the nūn is permitted), that is, the nūn of the dual and the plural, (along with governing) its governed term by putting it in the accusative as an object; unlike when it is annexed to it, for then its omission is obligatory,"},
    {"type": "matn",
     "ar": "(ومع التعريف[[٢]] تخفيفا) مفعول له للحذف، أي: يجوز حذفها بوجود هذين الشرطين لقصد مجرد التخفيف لطول الصلة بها،",
     "en": "(and with definiteness, for lightening): an object of purpose (mafʿūl lahu) for the omission; that is, its omission is permitted when these two conditions obtain, for the sole aim of lightening, because of the length of the relative clause (ṣila) with it,"},
    {"type": "matn",
     "ar": "كقراءة من قرأ: ﴿المقيمي الصلاة﴾[[٣]] بنصب «الصلاة» على المفعولية،",
     "en": "as in the reading of whoever read “those who establish the prayer” (al-muqīmī l-ṣalāta) with “al-ṣalāta” in the accusative as an object."},
    {"type": "matn",
     "ar": "وأما على تقدير التنكير مثل قوله تعالى: ﴿لذائقوا العذاب﴾[[٤]] بالنصب، فحذفها ضعيف؛ لأن اسم الفاعل لم يقع صلة اللام، والقراءة مما لا اعتماد عليه.",
     "en": "But on the supposition of indefiniteness, as in the words of the Exalted “you will surely taste the punishment” (la-dhāʾiqū l-ʿadhāba) with the accusative, its omission is weak, because the active participle has not occurred as the relative clause of the lām; and that reading is not one to be relied upon."},

    {"type": "section", "ar": "[اسم المفعول]",
     "en": "The Passive Participle"},

    {"type": "matn",
     "ar": "(اسم المفعول[[٥]]: هو ما اشتق من فعل) أي: حدث[[٦]] موضوعا (لمن وقع عليه[[٧]]) أي: لذات ما من حيث وقوع الفعل عليه،",
     "en": "(The passive participle (ism al-mafʿūl) is what is derived from a verb), that is, an event, being coined (for that upon which it falls), that is, for some entity in respect of the action’s falling upon it;"},
    {"type": "matn",
     "ar": "فـ«مضروب» موضوع لذات ما وقع عليها الضرب، واعتذار إقامة «من» مقام «ما» مر في اسم الفاعل.",
     "en": "so “maḍrūb” (struck) is coined for some entity upon which striking fell. The excuse for putting “man” in place of “mā” has been given under the active participle."},
    {"type": "matn",
     "ar": "فقوله: «ما اشتق من فعل» شامل لجميع الأمور المشتقة من المصدر.",
     "en": "His words “what is derived from a verb” include all things derived from the verbal noun (maṣdar)."},
    {"type": "matn",
     "ar": "وقوله: «لمن وقع عليه» يخرج ما عدا المحدود كاسم الفاعل، والصفة المشبهة، واسم التفضيل مطلقا، سواء وضع لتفضيل الفاعل أو لتفضيل المفعول، فإنه مشتق من",
     "en": "His words “for that upon which it falls” exclude everything other than the thing defined, such as the active participle, the resembling adjective (al-ṣifa al-mushabbaha) and the elative absolutely, whether coined for the preference of the agent or for the preference of the patient; for it is derived from…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وأما جمع المكسر فهو فرع الجمع السالم لكونه أشرف، فيتبعه في حكمه.",
     "en": "As for the broken plural, it is a branch of the sound plural, since the latter is nobler, so it follows it in its rule."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لام التعريف أي: ما تكون للتعريف في الجملة وإن لم تكن هنا.",
     "en": "That is, the lām of definiteness, that is, what serves for definiteness in general, even if it does not do so here."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الحج: ٣٥.",
     "en": "Qurʾān, Sūrat al-Ḥajj 22:35."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «سورة الحج: ٣٨», but «لذائقوا العذاب» is Sūrat al-Ṣāffāt 37:38; transcribed as printed.
    {"type": "pair",
     "ar": "سورة الحج: ٣٨.",
     "en": "Sūrat al-Ḥajj: 38 [as printed; translator’s reference: Qurʾān, Sūrat al-Ṣāffāt 37:38]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: المفعول به على حذف الجار، واستتار الضمير، يقال: فعلت به الضرب أوقعته عليه، وإلا فالمفعول هو الحدث.",
     "en": "That is, the “mafʿūl bihi” (that to which it is done), with the preposition omitted and the pronoun concealed; one says “faʿaltu bihi l-ḍarba” (I did striking to him), meaning “I made it fall upon him”; otherwise, what is done (al-mafʿūl) is the event itself."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سواء كان متعديا بنفسه أو بحرف الجر، وإن كان لازما غير متعد بحرف الجر، فلا يمكن بناء المفعول منه.",
     "en": "Whether it is transitive by itself or by a preposition; if it is intransitive and not made transitive by a preposition, the passive participle cannot be formed from it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "حقيقة أو اعتبارا ليشمل أوجدت ضربا، فهو موجد وعلمت عدم خروجك فهو معلوم،",
     "en": "Really or by consideration, so as to include “I brought a striking into existence”, so it is “brought into existence” (mūjad), and “I knew of your not going out”, so it is “known” (maʿlūm);"},
    {"type": "pair",
     "ar": "فإن الإيجاد والعلم تعلقا بالمعدوم، ولا معنى لوقوع الفعل على المعدوم حقيقة، لكن العقل يفسره واقعا عليه، ويعبر عنه بما يدل على الوقوع.",
     "en": "for bringing into existence and knowing are connected with the non-existent, and the action’s falling upon the non-existent has no real meaning; but the intellect interprets it as falling upon it and expresses it by what indicates falling."},
]
