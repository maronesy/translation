# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 357 (printed ٣٥٦)."""

PAGE_NUMBER = 357
PRINTED_PAGE = "٣٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «لأن جميعها ليست بمبنية بل بعضها.» at the foot of PDF p. 356 (new sentence).
    {"type": "matn",
     "ar": "فهذه ثمانية أبواب في بيان أسماء المبنية[[١]]، ولا بد لكل واحد منها من علة البناء؛ لأن الأصل في الأسماء الإعراب،",
     "en": "These, then, are eight chapters setting out the indeclinable nouns, and each one of them must have a cause of indeclinability (ʿillat al-bināʾ), because the default for nouns is inflection (iʿrāb)."},
    {"type": "matn",
     "ar": "وإذا كان مبنيا على الحركة فلا بد عند ذلك من علتين أخريين:",
     "en": "And when it is built on a vowel, two further causes are then required:"},
    {"type": "matn",
     "ar": "إحداهما: علة البناء على الحركة؛ لأن الأصل في البناء السكون.",
     "en": "the first is the cause of its being built on a vowel, because the default in indeclinability is quiescence (sukūn);"},
    {"type": "matn",
     "ar": "والأخرى: للحركة المعينة، إنها لما اختيرت دون الباقيتين؟",
     "en": "the other is [the cause] for the particular vowel: why was it chosen rather than the remaining two?"},

    {"type": "section", "ar": "[المضمر]",
     "en": "The Pronoun (al-Muḍmar)"},

    {"type": "matn",
     "ar": "(المضمر[[٢]]: ما وضع[[٣]] لمتكلم[[٤]]) من حيث إنه متكلم يحكي عن نفسه",
     "en": "(The pronoun (muḍmar) is what has been coined for a speaker), insofar as he is a speaker relating about himself,"},
    {"type": "matn",
     "ar": "(أو مخاطب) من حيث إنه مخاطب يتوجه إليه الخطاب.",
     "en": "(or an addressee), insofar as he is an addressee to whom the address is directed."},
    {"type": "matn",
     "ar": "وقيل: المراد بمتكلم من يتكلم به، أو بالمخاطب من يخاطب به، فإن «أنا» موضوع لمن يتكلم به، و«أنت» لمن يخاطب به،",
     "en": "It has also been said: what is meant by “a speaker” is the one who speaks with it, and by “the addressee” the one who is addressed with it; for “anā” (I) is coined for the one who speaks with it, and “anta” (you) for the one who is addressed with it."},
    {"type": "matn",
     "ar": "ويخرج بهذا القيد[[٥]] لفظ المتكلم والمخاطب،",
     "en": "By this qualification the words “speaker” and “addressee” are excluded,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: لا يشكل حصر المبني في هذه الثمانية بـ«ما» الشرطية والاستفهامية والصفة التامة، ومن أقسامها سوى الموصولة؛",
     "en": "He means: the restriction of the indeclinable to these eight is not problematized by conditional and interrogative “mā”, or [“mā” as] the complete qualifier, or the other kinds of it besides the relative,"},
    {"type": "pair",
     "ar": "لأن المراد بالموصولات ليس مجرد الموصولات، بل هو باب في بيان طائفة من الأسماء المبنية موصولات كانت أو غيرها،",
     "en": "because what is meant by “the relatives” is not the relatives alone; rather, it is a chapter setting out a group of indeclinable nouns, whether relatives or otherwise."},
    {"type": "pair",
     "ar": "ولا يشكل أيضا بفعال التي ليست بمعنى الأمر؛ لأن المراد بأسماء الأفعال ليست مجرد اسم الفعل، بل باب في بيان طائفة من الأسماء المبنية،",
     "en": "Nor is it problematized by [the pattern] faʿāli that does not carry an imperative sense, because what is meant by “the verbal nouns” (asmāʾ al-afʿāl) is not the verbal noun alone, but a chapter setting out a group of indeclinable nouns."},
    {"type": "pair",
     "ar": "ولا يشكل أيضا بخمسة في خمسة عشر، و«بعل» في بعلبك، فإنه مبني مع أنه لم يدخل في أقسام المبني؛",
     "en": "Nor, again, is it problematized by “khamsa” in “khamsata ʿashara” (fifteen) and “Baʿl” in “Baʿlabakk”, which are indeclinable although they do not fall under the divisions of the indeclinable,"},
    {"type": "pair",
     "ar": "لأن المركبات باب في بيان طائفة من الأسماء المبنية، ولا يقتصر على بيان المركبات",
     "en": "because “the compounds” is a chapter setting out a group of indeclinable nouns and is not confined to setting out compounds;"},
    {"type": "pair",
     "ar": "ولا بمثل وغير مع ما وأن وأن لدخولها هكذا في بعض الظروف.",
     "en": "nor by “mithl” and “ghayr” with “mā”, “an” and “anna”, since they fall in this way under “some adverbs” (baʿḍ al-ẓurūf)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قدمه على سائر المبنيات؛ إذ ليس في شيء منه إعراب، ولا نزاع في بنائه، وليس أيضا فيه فساد الالتباس.",
     "en": "He placed it before the other indeclinables because there is no inflection in any of it, there is no dispute over its indeclinability, and it is also free of the harm of ambiguity."},
    {"type": "pair",
     "ar": "وعلة بنائه احتياجه إلى حضور أو تقدم مكني عنه.",
     "en": "The cause of its indeclinability is its need for the presence, or prior mention, of what it stands in for."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: اسم وضع، فلا يرد النقض بمثل كاف ذلك.",
     "en": "That is: a noun that has been coined; so no counter-instance arises from such as the kāf of “dhālika”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "المشهور عند النحاة: وضع هذه الضمائر المفهوم المتكلم والمخاطب والغائب، وتحقيق وضعها لجزئيات معينة لهذه المفهومات،",
     "en": "The well-known view among the grammarians is that these pronouns are coined for the concept of speaker, addressee and absent person, while the precise view is that they are coined for particular individuals falling under these concepts;"},
    # REVIEW: the two Qurʾānic phrases below (al-Aʿrāf 7:144, Ibrāhīm 14:7) stand in the
    # gloss as printed, without an evident link to the argument; transcribed as printed.
    {"type": "pair",
     "ar": "والتعريف أظهر فيما هو التحقيق. وبهذا استغنيت عما تكلف الشارح لإخراجها، ﴿فخذ ما آتيتك وكن من الشاكرين﴾ (الأعراف: ١٤٤)،",
     "en": "and the definition is more apparent on what is the precise view. By this I have dispensed with the strain the commentator took to exclude them. “So take what I have given you and be among the grateful” (Qurʾān, Sūrat al-Aʿrāf 7:144)."},
    {"type": "pair",
     "ar": "وعلى طريقة النحاة ينبغي أن يحمل التعريف على أن المراد ما وضع ليستعمل في متكلم بعينه أو مخاطب أو غائب كذلك.",
     "en": "On the grammarians’ approach, the definition should be construed as meaning what is coined to be used for a specific speaker, or an addressee or absent person likewise."},
    {"type": "pair",
     "ar": "وبهذا أيضا اندفع لفظ المتكلم والمخاطب هذا ﴿لئن شكرتم لأزيدنكم﴾ (إبراهيم: ٧)،",
     "en": "By this, too, the words “speaker” and “addressee” are set aside. “If you are grateful, I will surely increase you” (Qurʾān, Sūrat Ibrāhīm 14:7)."},
    {"type": "pair",
     "ar": "وعلى التوجيهين لا بد من حمل متكلم وأخويه على الاستغراق والعموم، والنكرة قد يكون في الإثبات للعموم،",
     "en": "On both interpretations, “mutakallim” and its two sisters must be taken as all-inclusive and general; an indefinite noun may be general even in an affirmative context."},
    {"type": "pair",
     "ar": "والمراد بكلمة «ما» اسم، فلا ينتقض التعريف بحرف الخطاب.",
     "en": "What is meant by the word “mā” is a noun, so the definition is not broken by the particle of address."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: قوله به لفظا المتكلم والخطاب، فإنهما ليسا موضوعين للمتكلم والمخاطب بهما.",
     "en": "He means: [by] his words “bihi” the two words “speaker” and “address” [are excluded], for they are not coined for the one speaking with them and the one addressed with them."},
    {"type": "pair",
     "ar": "ولذا صح أنت متكلم، وأنا مخاطب.",
     "en": "Hence “anta mutakallim” (you are a speaker) and “anā mukhāṭab” (I am an addressee) are sound."},
    {"type": "pair",
     "ar": "وكذا يخرجان عن الحد بالتفسير السابق؛ لأن المراد بالمتكلم والمخاطب",
     "en": "Likewise they are excluded from the definition by the previous interpretation, because what is meant by “speaker” and “addressee”…"},
]
