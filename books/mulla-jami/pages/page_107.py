# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 107 (printed ١٠٦)."""

PAGE_NUMBER = 107
PRINTED_PAGE = "١٠٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فإن قلت: قد اعتبرت العجمة[[١]] في «ماه وجور» مع سكون الأوسط فيما سبق، فلم لم تعتبر ههنا؟",
     "en": "If you say: you took foreignness (ʿujma) into account in “Māh” and “Jūr,” together with the quiescence of the middle [letter], in what preceded; so why did you not take it into account here?"},
    {"type": "matn",
     "ar": "قلنا: اعتبارها فيما سبق، إنما هو لتقوية سببين[[٢]] آخرين، لئلا يقاوم سكون الأوسط أحدهما، ولا يلزم من اعتبارها لتقوية سبب آخر اعتبار سببيتها بالاستقلال.",
     "en": "We say: its being taken into account in what preceded was only to reinforce two other causes (sababayn), lest the quiescence of the middle counteract one of them; and its being taken into account to reinforce another cause does not entail taking its own causative status into account independently."},
    {"type": "matn",
     "ar": "(وشتر[[٣]]) وهو اسم حصن بديار بكر (وإبراهيم ممتنع) صرفهما لوجود الشرط الثاني فيهما، فإن في «شتر» تحرك الأوسط، وفي «إبراهيم» الزيادة على الثلاثة.",
     "en": "(And Shatar — which is the name of a fortress in Diyār Bakr — and Ibrāhīm: their [full] declension is prevented) on account of the presence of the second condition in both of them; for in “Shatar” there is the voweling of the middle [letter], and in “Ibrāhīm” augmentation beyond the three [radicals]."},
    {"type": "matn",
     "ar": "وإنما خص التفريع بالشرط الثاني؛ لأن غرضه التنبيه على ما هو الحق عنده من انصراف نحو: «نوح»، ولهذا قدم انصرافه مع أنه متفرع على انتفاء الشرط الثاني، والأولى تقديم[[٤]] ما هو متفرع على وجوده، كما لا يخفى.",
     "en": "He restricted the derivation (tafrīʿ) to the second condition only, because his aim was to alert [the reader] to what, in his view, is correct — namely the declinability of the like of “Nūḥ.” It is for this reason that he gave precedence to [mentioning] its declinability, even though that is derived upon the negation of the second condition, whereas it would have been more fitting to give precedence to what is derived upon its presence, as is not hidden."},
    {"type": "matn",
     "ar": "واعلم أن أسماء الأنبياء عليهم السلام[[٥]] ممتنعة عن الصرف إلا ستة: محمد، وصالح، وشعيب، وهود، لكونها عربية، ونوح، ولوط لخفتهما.",
     "en": "And know that the names of the prophets, upon them be peace, are prevented from full declension (i.e., are diptote) except for six: Muḥammad, Ṣāliḥ, Shuʿayb, and Hūd — because they are Arabic — and Nūḥ and Lūṭ — because of their lightness."},
    {"type": "matn",
     "ar": "وقيل: إن «هودا»[[٦]] ك«نوح»[[٧]]؛ لأن سيبويه قرنه معه، ويؤيده ما يقال من أن العرب من ولد إسماعيل، ومن كان قبل ذلك، فليس بعربي، و«هود» قبل إسماعيل فيما يذكر، فكان ك«نوح».",
     "en": "It has been said that “Hūd” is like “Nūḥ” [i.e., declinable only for its lightness, not as an Arabic name], because Sībawayh paired it with it; and this is supported by what is said — that the Arabs are the descendants of Ismāʿīl, and whoever was before that is not an Arab; and “Hūd” was before Ismāʿīl, according to what is reported, so he is like “Nūḥ.”"},

    {"type": "section", "ar": "[الجمع]",
     "en": "The Plural"},

    {"type": "matn",
     "ar": "(الجمع[[٨]]) وهو سبب[[٩]] قائم مقام السببين (شرطه) أي: شرط قيامه مقام",
     "en": "(The plural) — and it is a single cause standing in the place of two causes — (its condition), that is: the condition of its standing in the place of [the two causes …]"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا وأن يندفع بما ذكره، لكنه يرد أنك لم لم تعتبر المانعة من الصرف في ماه وجور العجمة بشرط التأنيث؟",
     "en": "This — granted it is warded off by what he mentioned — yet there still returns [the objection]: why did you not deem the factor preventing declension in “Māh” and “Jūr” to be foreignness under the condition of femininity (taʾnīth)?"},
    {"type": "pair",
     "ar": "ويدفعه ما سبق من ترجيح التأنيث على العجمة.",
     "en": "But it is warded off by what preceded, namely the giving of preponderance to femininity over foreignness."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لتقوية أحد سببين، وهو التأنيث؛ إذ العلمية مستغنية عن التقوية.",
     "en": "That is: to reinforce one of two causes, namely femininity; for proper-namehood (ʿalamiyya) has no need of reinforcement."},
    {"type": "pair",
     "ar": "ويدل على هذا قوله: «ولا يلزم من اعتبارها لتقوية سبب آخر» دون أن يقول لتقوية سببين.",
     "en": "This is indicated by his words, “and its being taken into account to reinforce another cause,” rather than his saying “to reinforce two causes.”"},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: يجوز أن يقال: امتناع صرفها لتأويلها بالبقعة. وفيه أنه لا يستعمل إلا مذكرا.",
     "en": "It has been said: it may be maintained that its being prevented from declension is on account of its being construed [figuratively] as “the plot of land” (al-buqʿa). But against this is that it (Shatar) is used only as masculine."},
    {"type": "pair",
     "ar": "ولا يرجع إليه ضمير المؤنث، وللمناقشة فيه مجال. فلو مثل بلمك اسم أبي نوح النبي عليه السلام لكان أسلم.",
     "en": "No feminine pronoun refers back to it, so there is room for dispute in it. Had he exemplified with “Lamak,” the name of the father of Nūḥ the prophet, upon him be peace, it would have been safer."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الواو للحال أو للعطف على مدخول كلمة مع، أي: ومع أن الأولى تقديم فرع الأمر الوجودي على العدمي.",
     "en": "The wāw [in “wa-l-awlā”] is for the circumstantial (ḥāl), or for conjoining to the object of the word “maʿa,” that is: “and although the more fitting course is to give precedence to the branch of the existential matter over the privative one.”"},
    {"type": "pair",
     "ar": "وهذا غير خاف؛ إذ الوجود أشرف خصال ومنبع كل كمل.",
     "en": "This is not hidden, since existence is the noblest of qualities and the wellspring of every perfection."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذه قاعدة مشهورة ذكر في كثير من كتب النحو، لكن ينقض بنحو: شيث وعزيز، فإنهما منصرفان كما يدل عليه النصوص.",
     "en": "This is a well-known rule, mentioned in many books of grammar; but it is refuted by the like of “Shīth” and “ʿAzīz,” for they are both declinable, as the texts indicate."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قائله الشيخ الرضي حيث قال: إن هودا مثل نوح في كونه أعجميا.",
     "en": "Its author is Shaykh al-Raḍī, where he said: “Hūd is like Nūḥ in being non-Arabic (aʿjamī).”"},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "اختير «نوح» في التمثيل لكونه اتفاقيا، وكون «هود» اختلافيا.",
     "en": "“Nūḥ” was chosen for the illustration because it is a matter of agreement [that it is declinable], while [the case of] “Hūd” is a matter of dispute."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هو كالمعرفة في الاشتراك بين الاسم وصفته. والمراد ههنا الصفة.",
     "en": "It [the term “the plural”] is like [the term] al-maʿrifa (the definite) in being shared between the [named] noun and its attribute; and what is intended here is the attribute."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: الجمعية، أو جمعية الجمع، أو الجمع من حيث إنه جمع.",
     "en": "That is: plurality (al-jamʿiyya), or the plurality of the plural, or the plural inasmuch as it is a plural."},
    {"type": "pair",
     "ar": "ويجوز أن يجعل اللام في الجمع للعهد، أي: جمعه يقوم مقام سببين، ليظهر تفسير الضمير في قوله: «شرطه» بما ذكره قدس سره.",
     "en": "It is also permissible to take the lām in “al-jamʿ” as denoting [prior] reference (al-ʿahd), that is: “its plural stands in the place of two causes,” so that the interpretation of the pronoun in his words “its condition (sharṭuhu)” by what he mentioned may become manifest — may his secret be sanctified."},
]
