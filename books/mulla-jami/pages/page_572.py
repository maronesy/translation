# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 572 (printed ٥٧١)."""

PAGE_NUMBER = 572
PRINTED_PAGE = "٥٧١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… إلا أنه لم يأت في العاطفة ما يلاقي الجزء الأخير، فإن» at the foot of PDF p. 571.
    {"type": "matn",
     "ar": "أصل «حتى» أن تكون جارة؛ لكثرة استعمالها، فتكون العاطفة محمولة عندهم على الجارة،",
     "en": "…the origin of “ḥattā” is that it be genitive-governing, because of its frequent use; so the coordinating [ḥattā] is, in their view, modelled on the genitive-governing one,"},
    {"type": "matn",
     "ar": "وإذا كانت محمولة عليها لم يستعملوها في معنييها جميعا؛ ليبقى للأصل على الفرع مزية،",
     "en": "and since it is modelled on it, they did not use it in both of its senses together, so that the original retains a distinction over the derivative;"},
    {"type": "matn",
     "ar": "وإنما استعملوها في أظهر معنييها، وهو كون مدخولها جزءا؛ لأن اتحاد الأجزاء في تعلق الحكم أعرف في العقل، وأكثر في الوجود من اتحاد المتجاورين.",
     "en": "they used it only in the more evident of its two senses, namely that what it enters upon is a part, because the union of parts in the attachment of a judgment is better known to the intellect, and more frequent in existence, than the union of two adjacent things."},
    {"type": "matn",
     "ar": "هكذا في بعض الشروح، ومن هذا ظهر وجه اختصاص معطوفها بكونه جزءا من متبوعه، وعدم الحاجة",
     "en": "So it is in some of the commentaries. From this the reason appears why what it coordinates is restricted to being a part of what it follows, and [why] there is no need [for that restriction to be stated otherwise],"},
    {"type": "matn",
     "ar": "إلا أن يقال: الجزء أعم من أن يكون حقيقة أو حكما، ليشتمل المجاور أيضا، كما وقع في بعض الحواشي.",
     "en": "unless it is said that the part is more general than being a part in reality or by legal fiction (ḥukman), so that it includes the adjacent as well, as occurs in some of the glosses."},
    # REVIEW: «وعدم الحاجة إلا أن يقال» — the sense of «وعدم الحاجة» is elliptical as printed; transcribed as printed.
    {"type": "matn",
     "ar": "(و«أو، وإما، وأم») كل من هذه الحروف الثلاثة (لأحد الأمرين[[١]]) أي: للدلالة على أحد الأمرين أو الأمور",
     "en": "(And “aw”, “immā” and “am”): each of these three particles is (for one of two things), that is, to indicate one of two things, or of several things,"},
    {"type": "matn",
     "ar": "حال كون ذلك الأحد (مبهما) أي: غير معين عند المتكلم[[٢]].",
     "en": "while that one is (indeterminate), that is, not specified in the mind of the speaker."},
    {"type": "matn",
     "ar": "ولا يتوهم أن «أو» في مثل قوله تعالى: ﴿ولا تطع منهم آثما أو كفورا﴾[[٣]] لكل من الأمرين[[٤]]؛",
     "en": "It should not be imagined that “aw” in such [an utterance] as His words, the Exalted, “and do not obey from among them a sinner or an ingrate” is for each of the two things;"},
    {"type": "matn",
     "ar": "لأنها مستعملة لأحد الأمرين على ما هو الأصل فيها، والعموم مستفاد من وقوع الأحد المبهم في سياق النفي لا من كلمة «أو».",
     "en": "for it is used for one of the two things, as is its original function, and the generality is derived from the indeterminate one’s occurring in the context of negation, not from the word “aw”."},
    {"type": "matn",
     "ar": "(وأم المتصلة[[٥]] لازمة لهمزة الاستفهام) أي غير مستعملة[[٦]] بدونها (يليها) أي:",
     "en": "(And the connected “am” (al-muttaṣila) is bound to the interrogative hamza), that is, it is not used without it; ([one of the two things] follows it), that is,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اكتفى المصنف في هذا المقام بأقل ما لا بد منه فلم يقل: أو الأمور،",
     "en": "Here the author contented himself with the least that is indispensable, and did not say “or several things”;"},
    {"type": "pair",
     "ar": "وله غير نظير في هذا الكتاب قال: الكلام ما تضمن كلمتين، وإذا تنازع الفعلان.",
     "en": "and he has more than one parallel to this in this book: he said “speech (kalām) is what contains two words”, and “when two verbs contend [for one governed term]”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بناء على أن الألفاظ لإفادة ما في الأذهان.",
     "en": "This is based on [the view] that utterances serve to convey what is in minds."},
    # REVIEW: printed «أما «لو» للتفصيل»; «لو» is unexpected here (one would expect «إما»); transcribed as printed.
    {"type": "pair",
     "ar": "قال العصام: هذا في «أو» للشك. أما «لو» للتفصيل كما في التقسيمات، و«أو» للإبهام، فهو لمعين عند المتكلم،",
     "en": "ʿIṣām [al-Dīn] said: this holds for “aw” of doubt. As for “law” for detailing (tafṣīl), as in divisions, and “aw” for deliberate vagueness (ibhām), it is for something specified in the mind of the speaker;"},
    {"type": "pair",
     "ar": "إلا أن يقال: إنه أراد بيان المعنى المشترك بين الثلاثة ومعنى التفصيل والإبهام لا يجري في «أم».",
     "en": "unless it is said that he meant to explain the sense shared by the three, and the sense of detailing and vagueness does not apply to “am”."},
    {"type": "pair",
     "ar": "وبهذا اندفع أنها في: ﴿ولا تطع منهم آثما أو كفورا﴾ (الإنسان: ٢٤) لكلا الأمرين؛",
     "en": "By this is repelled [the objection] that in “and do not obey from among them a sinner or an ingrate” (Qurʾān, Sūrat al-Insān 76:24) it is for both things;"},
    {"type": "pair",
     "ar": "لأنه لو سلم، فالكلام في المعنى المشترك بين الثلاثة، وهذا غير جار في أم",
     "en": "for even if that were granted, the discussion concerns the sense shared by the three, and this does not apply to “am”."},
    {"type": "pair",
     "ar": "وأما ما أجاب به عنه، فلا يدفع الاشتباه؛",
     "en": "As for the answer he gave to it, it does not remove the confusion;"},
    {"type": "pair",
     "ar": "لأنه وإن كان أو فيه لأحد الأمرين مبهما والعموم لزم من دخول النفي على أحد الأمرين مبهما، لكنه ليس لأحد الأمرين مبهما عند المتكلم.",
     "en": "for although “aw” in it is for one of two things indeterminately, and the generality follows from negation’s entering upon one of the two things indeterminately, it is nevertheless not for one of two things indeterminate in the mind of the speaker."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الإنسان: ٢٤.",
     "en": "Qurʾān, Sūrat al-Insān 76:24."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إذ لا يجوز أن يراد لا تطع واحدا منهما، وأطع الآخر بقرينة الإثم والكفر.",
     "en": "For it cannot be meant “do not obey one of them, and obey the other”, given the contextual indication (qarīna) of sin and unbelief."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أراد أن يبين الفرق بين الثلاثة وبدأ من القريب.",
     "en": "He wanted to explain the difference between the three, and began with the nearest."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن اللازم بالمعنى اللغوي، وليس بالمعنى المصطلح بين أرباب المعقول المفسر بما يمتنع انفكاكه عن الشيء",
     "en": "He means that “bound” (lāzim) is in the lexical sense, not in the sense current among the masters of the rational sciences, defined as that whose separation from the thing is impossible,"},
    {"type": "pair",
     "ar": "حتى يرد أن الصواب، وأم المتصلة ملزومة لهمزة الاستفهام؛ لأنه حيث استعملت أم المتصلة استعملت دون العكس.",
     "en": "so that the objection would arise that the correct [wording] is “and the connected ‘am’ entails (malzūma) the interrogative hamza”, since wherever the connected “am” is used, [the hamza] is used, but not the reverse."},
]
