# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 138 (printed ١٣٧)."""

PAGE_NUMBER = 138
PRINTED_PAGE = "١٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "أما في صورة اتصال ضمير المفعول به: لئلا يلزم الإضمار قبل الذكر لفظا ورتبة[[١]].",
     "en": "As for the case where the object-pronoun is affixed to it [the verb]: [postposing the agent is required] so that pronominalization does not occur before the antecedent’s mention, either in wording or in rank."},
    {"type": "matn",
     "ar": "وأما في صورة وقوعه بعد «إلا» أو معناها: لئلا ينقلب الحصر المطلوب[[٢]].",
     "en": "As for the case where it falls after “illā” or its meaning: so that the intended restriction is not inverted."},
    {"type": "matn",
     "ar": "وأما في صورة كون المفعول ضميرا متصلا، والفاعل غير متصل: لمنافاة الاتصال توسط الفاعل الغير المتصل بينه وبين الفعل، بخلاف ما إذا كان الفاعل أيضا ضميرا متصلا، فإنه يجب حينئذ تقديم الفاعل، نحو: «ضربتك».",
     "en": "As for the case where the object is an affixed pronoun while the agent is not affixed: it is because affixation is incompatible with the interposition of the non-affixed agent between it and the verb — unlike when the agent too is an affixed pronoun, for then fronting the agent becomes obligatory, as in “I struck you” (ḍarabtuka)."},

    {"type": "section", "ar": "[ حذف الفعل ]",
     "en": "The Elision of the Verb"},

    {"type": "matn",
     "ar": "(وقد يحذف الفعل) الرافع للفاعل (لقيام قرينة[[٣]]) دالة على تعيين المحذوف:",
     "en": "“The verb” — the one that governs the agent — “may be elided owing to the presence of a contextual indicator (qarīna)” that specifies the elided element:"},
    {"type": "matn",
     "ar": "١-(جوازا) أي: حذفا جائزا[[٤]] (في مثل) قولك: (زيد[[٥]]) أي: فيما كان جوابا لسؤال[[٦]] محقق (لمن قال: «من قام؟») سائلا عمن يقوم به القيام، فيجوز أن تقول: «زيد» بحذف «قام» أي: «قام زيد»، ويجوز أن تقول: «قام زيد» بذكره.",
     "en": "(1) “Optionally” — that is, an admissible elision — “in the like of” your saying: “Zayd,” meaning in what is an answer to an actual question, addressed “to one who says: Who stood?”, asking about the one by whom the standing occurs. So you may say “Zayd,” eliding “stood” — i.e., “Zayd stood” — and you may say “Zayd stood,” mentioning it."},
    {"type": "matn",
     "ar": "وإنما قدر الفعل دون الخبر؛ لأن تقدير الخبر يوجب حذف الجملة، وتقدير الفعل يوجب حذف جزئها، والتقليل في الحذف أولى.",
     "en": "The verb, rather than a predicate, is what is taken to be implied, because supposing a predicate would entail the elision of a whole sentence, whereas supposing a verb entails the elision of only one of its parts — and minimizing elision is preferable."},
    {"type": "matn",
     "ar": "(و) كذا يحذف الفعل جوازا فيما كان جوابا لسؤال مقدر في نحو قول الشاعر في مرثية يزيد بن نهشل: (ليبك) على البناء للمفعول (يزيد) مرفوع[[٧]] على أنه مفعول ما لم...",
     "en": "“And” likewise the verb is elided optionally in what is an answer to an implied question, as in the poet’s words elegizing Yazīd b. Nahshal: “Let there be wept” — in the passive voice — “Yazīd,” nominative as the deputy-subject (nāʾib al-fāʿil) of a [passive] verb whose…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ينبغي أن يكون في وجوب تأخير الفاعل في هذه الصورة خلاف الأخفش وابن جني.",
     "en": "In the obligation of postposing the agent in this case there ought to be a disagreement of al-Akhfash and Ibn Jinnī."},
    {"type": "pair",
     "ar": "أما على ما ذكره الشارح فلجواز الإضمار قبل الذكر عندهما. وأما على ما نقلناه من مذهبيهما فلأن رتبة المفعول عندهما أن يلي الفعل، ويكون في موضع الفاعل فلم يلزم من تأخيره الإضمار قبل الذكر رتبة، فتأمل.",
     "en": "As for what the commentator mentioned, [the obligation holds for them] because pronominalization before mention is permissible according to the two of them. As for what we have transmitted of their two schools: because in their view the rank of the object is to immediately follow the verb and to occupy the position of the agent, so its postposing does not entail pronominalization before mention in rank — so ponder it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن مضروبية ما قبل إلا محصورة فيما بعدها، والضاربية محتملة، فلو قدم الفاعل لانعكس المعنى.",
     "en": "Because the object-hood (being-struck) of what precedes “illā” is confined to what comes after it, whereas the agent-hood (being-striker) is merely possible; so were the agent fronted the meaning would be reversed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مقام الفعل في الدلالة على ما هو المرام. واللام للوقت لا للأجل؛ لأن قيام القرينة مصحح لا باعث.",
     "en": "[The indicator] stands in the place of the verb in signifying what is intended. The lām [in “li-qiyāmi”] denotes the time, not the purpose, because the presence of the indicator is a validating factor, not a motivating cause."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إشارة إلى أن «جوازا» مصدر بمعنى اسم الفاعل، ونصبه على المصدرية باعتبار موصوفه الذي هو الحذف.",
     "en": "An indication that “jawāzan” is a verbal noun with the sense of an active participle, and its accusative is as an absolute object (maṣdar) by consideration of its described term, which is the elision."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "خبر مبتدأ محذوف، أي: هو في مثل كما هو الشائع في التمثيلات.",
     "en": "[It is] the predicate of an elided subject — i.e., “it is in the like of…” — as is customary in [giving] illustrations."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وكون السؤال قرينة إنما هو باعتبار جزئه الذي هو «قام». وقوله: «فيجوز» مع ما عطف عليه تفريع على كون المثال مما يجوز فيه الحذف.",
     "en": "The question’s being an indicator is only by consideration of its part, which is “stood.” And his words “so it is permissible,” together with what is conjoined to it, are a corollary drawn from the example’s being of the kind in which elision is permissible."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "والأصل على «يزيد»؛ لأن البكاء يتعدى بـ«على»، لكنها تحذف لكثرة الاستعمال.",
     "en": "The original is “upon Yazīd” (ʿalā Yazīd), for weeping (bukāʾ) takes its object by means of “ʿalā”; but it is dropped owing to frequency of use."},
    {"type": "pair",
     "ar": "نقل عن العارف الرومي قدس سره: أن «يزيد» منادى بحذف حرف النداء، والجملة الندائية معترضة. وذلك لأن...",
     "en": "It is transmitted from the gnostic al-Rūmī, may his secret be sanctified, that “Yazīd” is a vocative with the vocative particle elided, the vocative clause being parenthetical. And that is because…"},
]
