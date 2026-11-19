# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 171 (printed ١٧٠)."""

PAGE_NUMBER = 171
PRINTED_PAGE = "١٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "إلى الإنشائية[[١]]، ويؤيده قوله تعالى: ﴿إن الذين كفروا وماتوا وهم كفار فلن يقبل﴾[[٢]].",
     "en": "…to the performative (inshāʾiyya); and it is supported by His words, the Exalted: “Truly those who disbelieve and die while they are disbelievers—it shall not be accepted (fa-lan yuqbala)…”"},
    {"type": "matn",
     "ar": "فإن قيل: قد ألحق بعضهم «أن» المفتوحة و«لكن» بـ«ليت» و«لعل»، فما وجه تخصيص «إن» المكسورة بالإلحاق؟",
     "en": "If it is said: some have attached “anna” with fatḥa and “lākinna” to “layta” and “laʿalla”; so what is the reason for singling out “inna” with kasra for the attachment?"},
    {"type": "matn",
     "ar": "قيل: بعضهم الذي ألحق «إن» بهما هو سيبويه[[٣]]، فاعتد بقوله وذكره، ولم يعتد بقول من سواه، فلم يذكره،",
     "en": "It is said: the “some” who attached “inna” to the two of them is Sībawayh; so he took account of his view and mentioned it, and did not take account of the view of anyone besides him, and so did not mention it;"},
    {"type": "matn",
     "ar": "مع أن كلا القولين لا يساعدهما القرآن وكلام الفصحاء[[٤]]،",
     "en": "although neither of the two views is borne out by the Qurʾān and the speech of the eloquent (al-fuṣaḥāʾ)."},
    {"type": "matn",
     "ar": "فما يدل على عدم منع «إن» المكسورة عن دخول الفاء على الخبر ما سبق،",
     "en": "What shows that “inna” with kasra does not prevent the entry of the fāʾ upon the predicate is what has preceded;"},
    {"type": "matn",
     "ar": "وما يدل على عدم منع «أن» المفتوحة و«لكن» عن دخول الفاء قوله تعالى: ﴿واعلموا أنما غنمتم من شيء فأن لله خمسه﴾[[٥]]، وقول الشاعر:",
     "en": "and what shows that “anna” with fatḥa and “lākinna” do not prevent the entry of the fāʾ is His words, the Exalted: “And know that whatever spoils you take, a fifth of it belongs to Allah (fa-anna li-llāhi khumusahu),” and the poet’s words:"},
    {"type": "verse",
     "ar": "فوالله ما فارقتكم قاليا لكم        ولكن ما يقضى فسوف يكون",
     "en": "“By Allah, I did not part from you out of loathing for you; but what is decreed shall come to be (fa-sawfa yakūnu).”"},

    {"type": "section", "ar": "[ حذف المبتدأ والخبر ]",
     "en": "The Elision of the Subject and the Predicate"},

    {"type": "matn",
     "ar": "(وقد يحذف المبتدأ لقيام قرينة[[٦]]) لفظية أو عقلية (جوازا) أي: حذفا جائزا لا واجبا.",
     "en": "(The subject may be elided when a contextual indicator is present—wa-qad yuḥdhafu al-mubtadaʾu li-qiyāmi qarīnatin), whether verbal or rational, (optionally—jawāzan), that is: as a permissible, not an obligatory, elision."},
    {"type": "matn",
     "ar": "وقد يجب حذفه[[٧]] إذا قطع النعت بالرفع[[٨]]، نحو: «الحمد لله أهل الحمد»",
     "en": "Its elision is sometimes obligatory, when the qualifier (naʿt) is cut off [from its head] in the nominative, as in: “Praise belongs to Allah, the One worthy of praise (ahlu al-ḥamdi)”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أنه صرح آنفا أن باب «كان» وباب «علمت» مانعان بالاتفاق مع أنهما لا يخرجان الكلام من الخبرية إلى الإنشائية،",
     "en": "There is [an objection] to this: he stated explicitly just above that the class of “kāna” and the class of “ʿalimtu” prevent [the fāʾ] by agreement, although they do not take the utterance out of the declarative (khabariyya) into the performative (inshāʾiyya);"},
    {"type": "pair",
     "ar": "فلم ينحصر علة الحكم في ذلك، فالاستدلال على عدم المنع بعدم الإخراج من الخبرية إلى الإنشائية ليس بصحيح.",
     "en": "so the cause (ʿilla) of the ruling is not confined to that, and inferring the absence of prevention from the absence of taking [the utterance] out of the declarative into the performative is not sound."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة آل عمران، ٩١.",
     "en": "Qurʾān, Sūrat Āl ʿImrān 3:91."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "نقل عن المصنف أنه قال في الإيضاح: منع سيبويه من دخول الفاء في خبر «إن» بعيد من جهة النقل والفقه.",
     "en": "It is reported from the author that he said in al-Īḍāḥ: Sībawayh’s prohibition of the entry of the fāʾ into the predicate of “inna” is far-fetched from the standpoint of both transmission (naql) and understanding (fiqh)."},
    {"type": "pair",
     "ar": "أما النقل، فقد استشهد سيبويه في كتابه بعد قوله: ﴿الذين ينفقون أموالهم﴾ بقوله: ﴿قل إن الموت الذي﴾ (سورة الجمعة:٨).",
     "en": "As for transmission: Sībawayh in his Book, after His words “Those who spend their wealth…,” cited as evidence His words “Say: truly the death which…” (Qurʾān, Sūrat al-Jumuʿa 62:8)."},
    {"type": "pair",
     "ar": "وأما الفقه، فيبعد منه وقوعه في مخالفة الواضحات.",
     "en": "As for understanding: it is unlikely of him that he would fall into contradicting what is plain."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ذهب هذا البعض إلى منع هذه الحروف من دخول الفاء في الخبر مع عدم مساعدة القرآن وكلام الفصحاء كذلك في غاية القبح.",
     "en": "That these “some” held that these particles prevent the entry of the fāʾ into the predicate, although the Qurʾān and the speech of the eloquent do not bear this out, is utterly unseemly."},
    {"type": "pair",
     "ar": "والنحاة استنبطوا قواعد النحو من كلام الفصحاء، فكيف يخالفون في الحكم بكلام الفصحاء؟",
     "en": "The grammarians derived the rules of syntax (naḥw) from the speech of the eloquent; how then can they contradict the speech of the eloquent in a ruling?"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة الأنفال:٤١.",
     "en": "Qurʾān, Sūrat al-Anfāl 8:41."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "اللام للوقت لا للأجل؛ لأنه مصحح لا مقتض وداع، والدواعي مذكورة في علم البلاغة.",
     "en": "The lām [in li-qiyāmi] is temporal, not causal; for [the indicator] is what makes [the elision] valid, not what requires and motivates it; the motives are treated in the science of rhetoric (ʿilm al-balāgha)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيل: لا يجب حذفه أصلا؛ لأنه ركن أصيل في الكلام،",
     "en": "It has been said: its elision is never obligatory, because it is a fundamental pillar of the utterance;"},
    {"type": "pair",
     "ar": "ونحو: «الحمد لله أهل الحمد» محمول على حذف الخبر أي: أهل الحمد هو،",
     "en": "and such as “Praise belongs to Allah, the One worthy of praise” is to be construed as an elision of the predicate, that is: “the One worthy of praise is He”;"},
    {"type": "pair",
     "ar": "والقول بأن المخصوص بالمدح أو الذم خبر مما لا يعتد به.",
     "en": "and the view that the specified object of praise or blame (al-makhṣūṣ bi-l-madḥ aw al-dhamm) is a predicate is not taken into account."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: يجعل إعرابه مخالفا لإعراب المنعوت.",
     "en": "That is: its inflection (iʿrāb) is made to differ from the inflection of the qualified noun (al-manʿūt)."},
]
