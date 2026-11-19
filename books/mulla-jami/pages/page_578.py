# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 578 (printed ٥٧٧)."""

PAGE_NUMBER = 578
PRINTED_PAGE = "٥٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(و«بلى» مختصة بإيجاب النفي) يعني: ينقض النفي المتقدم، ويجعله إيجابا سواء»
    # at the foot of PDF p. 577 (mid-sentence).
    {"type": "matn",
     "ar": "كان ذلك النفي مجردا عن الاستفهام نحو: «بلى» في جواب من قال: «ألم يقم زيد» أي: قد قام زيد،",
     "en": "…that negation is free of interrogation, as with “balā” in answer to one who says “alam yaqum Zaydun” (Zayd has not stood), that is: Zayd has indeed stood;"},
    {"type": "matn",
     "ar": "أو مقرونا به، فهي إذن لنقض النفي الذي بعد ذلك الاستفهام، كقوله تعالى: ﴿ألست بربكم قالوا بلى﴾[[١]] أي: بلى أنت ربنا.",
     "en": "or joined to it, in which case it serves to cancel the negation that follows that interrogation, as in His words, the Exalted: “Am I not your Lord? They said: Yes (balā)”, that is: yes, You are our Lord."},
    {"type": "matn",
     "ar": "وقد جاء على سبيل الشذوذ، لتصديق الإيجاب كما تقول في جواب: «أقام زيد؟»: بلى، أي: قام زيد.",
     "en": "It has occurred, anomalously (ʿalā sabīl al-shudhūdh), to confirm an affirmative, as when you say in answer to “aqāma Zaydun?” (did Zayd stand?): “balā”, that is: Zayd stood."},
    {"type": "matn",
     "ar": "(و«إي» إثبات بعد الاستفهام) ولا شك في غلبة استعمالها مسبوقة بالاستفهام.",
     "en": "(And “ī” is an affirmation after an interrogation). There is no doubt that it is predominantly used preceded by an interrogation."},
    {"type": "matn",
     "ar": "وذكر بعضهم: أنها تجيء لتصديق الخبر أيضا. وذكر ابن مالك: أن «إي» بمعنى: «نعم»، وهذا مخالف لما ذكره المصنف:",
     "en": "Some have mentioned that it also comes to confirm a statement (khabar). Ibn Mālik mentioned that “ī” is in the sense of “naʿam”; and this differs from what the author mentioned:"},
    {"type": "matn",
     "ar": "(ويلزمها القسم) أي: لا تستعمل إلا مع القسم من غير ذكر فعل القسم، فلا يقال: «إي أقسمت بربي»،",
     "en": "(and the oath accompanies it necessarily), that is, it is used only with an oath, without mention of the verb of swearing; so one does not say “ī aqsamtu bi-rabbī” (yes, I swore by my Lord);"},
    {"type": "matn",
     "ar": "ولا يكون المقسم به إلا «الرب، والله، ولعمري»، تقول: «إي والله، وإي وربي، وإي لعمري».",
     "en": "and the thing sworn by is only “al-rabb” (the Lord), “Allāh” and “la-ʿamrī” (by my life); you say: “ī wa-llāhi” (yes, by Allah), “ī wa-rabbī” (yes, by my Lord) and “ī la-ʿamrī” (yes, by my life)."},
    {"type": "matn",
     "ar": "(و«أجل»، و«جير») بالكسر والفتح.",
     "en": "(And “ajal” and “jayr”), [the latter] with kasra and with fatḥa [on the final rāʾ]."},
    {"type": "matn",
     "ar": "(و«إن» تصديق للمخبر) وفي بعض النسخ: تصديق للخبر",
     "en": "(And “inna” are a confirmation of the one who informs); in some copies: a confirmation of the statement;"},
    {"type": "matn",
     "ar": "كقولك: «أجل، أو جير أو إن» للمخبر «قد أتاك زيد، أو لم يأتك»، أي: قد أتى، أو لم يأت.",
     "en": "as when you say “ajal”, or “jayr”, or “inna” to one who informs you “Zayd has come to you” or “has not come to you”, that is: he has indeed come, or he has not come."},
    {"type": "matn",
     "ar": "وجاء «إن» لتصديق الدعاء أيضا، نحو قول ابن الزبير لمن قال: «لعن الله ناقة حملتني إليك»: إن وراكبها، أي: «لعن الله تلك الناقة وراكبها».",
     "en": "“Inna” has also come to confirm an imprecation (duʿāʾ), as in the words of Ibn al-Zubayr to one who said “May Allah curse a she-camel that carried me to you”: “inna wa-rākibahā” (yes, and her rider), that is: “May Allah curse that she-camel and her rider.”"},
    {"type": "matn",
     "ar": "وجاء بعد الاستفهام أيضا في قول الشاعر:",
     "en": "It has also come after an interrogation, in the words of the poet:"},
    {"type": "verse",
     "ar": "ليت شعري هل للمحب شفاء     من جوى حبهن إن اللقاء",
     "en": "Would that I knew: is there a cure for the lover from the ardour of his love for them? — Yes (inna): the meeting."},
    {"type": "matn",
     "ar": "أي: «نعم اللقاء شفاء للمحب»، فمجيئها في هذين الموضعين خلاف ما ذكره المصنف من كونها تصديقا للمخبر.",
     "en": "That is: “Yes, meeting is a cure for the lover.” Its occurrence in these two places is contrary to what the author mentioned, namely its being a confirmation of the one who informs."},

    {"type": "section", "ar": "[حروف الزيادة]",
     "en": "The Particles of Redundancy (ḥurūf al-ziyāda)"},

    {"type": "matn",
     "ar": "(حروف الزيادة) وإنما سميت هذه الحروف زوائد؛ لأنها قد تقع زائدة، لا أنها لا تقع إلا زائدة.",
     "en": "(The particles of redundancy). These particles are called redundant (zawāʾid) only because they sometimes occur as redundant, not because they occur only as redundant."},
    {"type": "matn",
     "ar": "ومعنى كونها زائدة: أن أصل المعنى بدونها لا يختل، لا أنها لا فائدة لها أصلا،",
     "en": "The meaning of their being redundant is that the basic meaning is not impaired without them, not that they have no benefit at all;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الأعراف: ١٧٢.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:172."},
]
