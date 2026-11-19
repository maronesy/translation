# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 235 (printed ٢٣٤)."""

PAGE_NUMBER = 235
PRINTED_PAGE = "٢٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the sentence «لأنهم لم يوقعوا» from the foot of PDF p. 234.
    {"type": "matn",
     "ar": "فيها فعلا، بل الكرام الكاتبون أوقعوا فيها كتابة أفعالهم،",
     "en": "…any deed in them; rather, the noble scribes (al-kirām al-kātibūn) placed in them the record of their deeds."},
    {"type": "matn",
     "ar": "وإن كان صفة لـ«شيء» مع أنه خلاف ظاهر الآية فات المعنى المقصود؛",
     "en": "And if it is a qualifier of “shayʾ” (thing)—besides being contrary to the apparent sense of the verse—the intended meaning is lost;"},
    {"type": "matn",
     "ar": "إذ المقصود: إن كل شيء هو مفعول لهم كائن في الزبر مكتوب فيها؛ موافقا لقوله تعالى: ﴿وكل صغير وكبير مستطر﴾[[١]]،",
     "en": "for what is intended is that everything done by them is in the scriptures (al-zubur), written in them, in agreement with His words, the Exalted: “And everything, small and great, is inscribed” (Qurʾān, Sūrat al-Qamar 54:53);"},
    {"type": "matn",
     "ar": "لا أن كل شيء كائن في صحائف أعمالهم مفعول لهم،",
     "en": "not that everything that is in the scrolls of their deeds was done by them."},
    {"type": "matn",
     "ar": "فالرفع لازم على أن يكون «كل شيء» مبتدأ، والجملة الفعلية صفة لـ«شيء»، والجار والمجرور في محل الرفع على أنه خبر المبتدأ،",
     "en": "So the nominative is necessary, “kullu shayʾin” being a mubtadaʾ (subject), the verbal sentence a qualifier of “shayʾ,” and the preposition with its genitive in the position of the nominative as the khabar (predicate) of the mubtadaʾ;"},
    {"type": "matn",
     "ar": "تقديره: «كل شيء هو مفعول لهم ثابت في الزبر بحيث لا يغادر[[٢]] صغيرة ولا كبيرة».",
     "en": "its implied form is: “Everything that is done by them is established in the scriptures, such that it leaves out nothing small or great.”"},
    {"type": "matn",
     "ar": "واعلم أنه قد سبق أن الاسم المذكور إذا كان الفعل المشتغل عنه بضميره أو متعلقه أمرا أو نهيا فالمختار فيه النصب،",
     "en": "Know that it has already been stated that, when the verb diverted from the mentioned noun by its pronoun or by what is connected to it is a command or a prohibition, the accusative is preferred in it;"},
    {"type": "matn",
     "ar": "والظاهر[[٣]] أن قوله تعالى: ﴿الزانية والزاني فاجلدوا كل واحد منهما مائة جلدة﴾[[٤]] داخل تحت هذه القاعدة",
     "en": "and it appears that His words, the Exalted, “The adulteress and the adulterer: flog each one of them a hundred lashes” (Qurʾān, Sūrat al-Nūr 24:2) fall under this rule,"},
    {"type": "matn",
     "ar": "مع أن القراء اتفقوا فيه على الرفع، إلا في رواية شاذة عن بعضهم[[٥]]،",
     "en": "although the Qurʾān readers (al-qurrāʾ) agreed on the nominative in it, except in an anomalous (shādhdh) transmission from one of them."},
    {"type": "matn",
     "ar": "فاضطر النحاة إلى أن تمحلوا لإخراجه عن هذه القاعدة المذكورة؛ لئلا يلزم اتفاق القراء على غير المختار،",
     "en": "So the grammarians were compelled to contrive [explanations] to remove it from this stated rule, lest it follow that the readers agreed on what is not preferred."},
    {"type": "matn",
     "ar": "فأشار المصنف إلى ما تمحلوا لإخراجه عنها فقال: (ونحو: ﴿الزانية والزاني[[٦]] فاجلدوا كل واحد منهما﴾[[٧]] الفاء) فيه مرتبط (بمعنى الشرط[[٨]] عند المبرد[[٩]]) لكون الألف واللام",
     "en": "The author pointed to what they contrived to remove it from [the rule], saying: (And such as “The adulteress and the adulterer: flog each one of them”—the fāʾ) in it is linked (to the sense of the condition, according to al-Mubarrad), because the alif and lām…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة القمر: ٥٣.",
     "en": "Qurʾān, Sūrat al-Qamar 54:53."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا يترك سيئة كبيرة ولا صغيرة.",
     "en": "That is: it does not leave out any evil deed, great or small."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يمنع الفاء بحسب الظاهر دخوله في هذا الباب؛ لأن ما بعدها قد يعمل فيما قبلها نحو قوله تعالى: ﴿وربك فكبر﴾ (سورة المدثر: ٣).",
     "en": "The fāʾ does not, by the apparent sense, prevent its entering this chapter, because what follows it may govern what precedes it, as in His words, the Exalted: “And your Lord, magnify” (Qurʾān, Sūrat al-Muddaththir 74:3)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة النور: ٢.",
     "en": "Qurʾān, Sūrat al-Nūr 24:2."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: print reads «عيسى ابن عمرو»; the reader of the accusative is usually named ʿĪsā ibn ʿUmar (al-Thaqafī); transcribed as printed.
    {"type": "pair",
     "ar": "هو عيسى ابن عمرو.",
     "en": "He is ʿĪsā ibn ʿAmr."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الواو إما للعطف على كل شيء فعلوه، فيكون التقدير: وكذا نحو: ﴿الزانية والزاني﴾،",
     "en": "The wāw is either for conjunction with “kullu shayʾin faʿalūhu,” so the implied form is: “and likewise such as ‘The adulteress and the adulterer’”;"},
    {"type": "pair",
     "ar": "وقوله الفاء بمعنى الشرط تعليل، وجملة قوله: وجملتان بتقدير المبتدأ أي: هذه الآية جملتان تعليل آخر معطوف على الأول،",
     "en": "his words “the fāʾ in the sense of the condition” are then a justification (taʿlīl), and the sentence of his words “and two sentences,” by supplying the mubtadaʾ—that is, “this verse is two sentences”—is another justification conjoined to the first."},
    {"type": "pair",
     "ar": "وإما للعطف على قوله: وكذا ﴿وكل شيء فعلوه﴾ (القمر: ٥٢)،",
     "en": "Or it is for conjunction with his words “and likewise ‘And everything they did’” (Qurʾān, Sūrat al-Qamar 54:52);"},
    {"type": "pair",
     "ar": "وجملة قوله الفاء بمعنى الشرط المشيرة إلى التعليل خبر لقوله نحو: ﴿الزانية﴾، بتقدير العائد،",
     "en": "then the sentence of his words “the fāʾ in the sense of the condition,” which points to the justification, is the predicate of his words “such as ‘The adulteress’,” by supplying the returning pronoun (al-ʿāʾid);"},
    {"type": "pair",
     "ar": "وقوله: جملتان معطوف عليها عطف مفرد على جملة لها محل من الإعراب.",
     "en": "and his words “two sentences” are conjoined to it, as the conjunction of a single term to a sentence that has a place in iʿrāb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة النور: ٢.",
     "en": "Qurʾān, Sūrat al-Nūr 24:2."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فتكون الباء صلة. ويجوز أن تكون للسببية.",
     "en": "So the bāʾ is redundant (ṣila); it may also be causal."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "قيل: ظرف لعامل الظرف المقدر. والأظهر أنه ظرف للنسبة بين المبتدأ والخبر",
     "en": "It has been said: [“ʿinda”] is an adverbial for the governor of the implied adverbial. The more evident [view] is that it is an adverbial for the predicative relation between the mubtadaʾ and the khabar,"},
    {"type": "pair",
     "ar": "كما أن قوله عند سيبويه ظرف للنسبة بين المبتدأ والخبر، يوافق قوله تعالى: ﴿إن الدين عند الله الإسلام﴾ (سورة آل",
     "en": "just as his words “according to Sībawayh” are an adverbial for the relation between the mubtadaʾ and the khabar, agreeing with His words, the Exalted: “Truly, the religion with Allah is Islam” (Sūrat Āl…"},
]
