# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 440 (printed ٤٣٩)."""

PAGE_NUMBER = 440
PRINTED_PAGE = "٤٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لأنه على تقدير تسليمه إذا دل أمران من أمور ثلاثة» at the foot of PDF p. 439 (mid-sentence).
    {"type": "matn",
     "ar": "على شيء صح أن يقال[[١]]: هذه الأمور الثلاثة دالة عليه. غاية ما في الباب أن يكون دلالتها بواسطة هذين الأمرين",
     "en": "…something, it is correct to say: these three things indicate it. The most that can be said is that their indication is by means of these two things."},
    {"type": "matn",
     "ar": "(على أن معه) أي: مع مفرده[[٢]] (مثله) في العدد، يعني: الواحد[[٣]] حال كون ذلك المثل (من جنسه) أي: من جنس مفرده",
     "en": "(That with it), that is, with its singular, (is its like) in number, meaning one, that like being (of its genus), that is, of the genus of its singular,"},
    {"type": "matn",
     "ar": "باعتبار دخوله[[٤]] تحت جنس الموضوع له[[٥]] بوضع واحد مشترك بينهما[[٦]]،",
     "en": "in that it falls under the genus of that for which [the word] is coined, by a single coinage (waḍʿ) common to both."},
    {"type": "matn",
     "ar": "ولو أريد بقوله: «مثله» ما يماثله في الوحدة والجنس جميعا لاستغنى[[٧]] عن قوله: «من جنسه»[[٨]]،",
     "en": "Had “its like” been meant as what resembles it in both unity and genus together, he would have had no need of his words “of its genus”."},
    {"type": "matn",
     "ar": "وقوله: «ليدل» إشارة إلى فائدة لحوق هذه الحروف بالاسم المفرد، وإلى أنه لا يجوز تثنية الاسم باعتبار معنيين مختلفين،",
     "en": "His words “so as to indicate” point to the benefit of attaching these letters to the singular noun, and to the fact that a noun may not be put in the dual with respect to two different meanings."},
    {"type": "matn",
     "ar": "فلا يقال: «قرآن» ويراد بها الطهر والحيض، بل يراد بها طهران أو حيضان على الصحيح، خلافا لبعضهم.",
     "en": "So one does not say “qurʾān” (two quruʾ) meaning a period of purity and a menstruation; rather, it means two periods of purity or two menstruations, according to the sound view, contrary to some."},
    {"type": "matn",
     "ar": "فإن قلت: هذا[[٩]] يشكل بـ«الأبوين» للأب والأم، و«القمرين» للقمر والشمس،",
     "en": "If you say: this is problematic in view of “al-abawayn” (the two fathers) for father and mother, and “al-qamarayn” (the two moons) for the moon and the sun;"},
    {"type": "matn",
     "ar": "فإنه يثنى الأب باعتبار معنيين مختلفين -هما الأب والأم- وكذلك يثنى القمر باعتبار معنيين مختلفين هما القمر والشمس؟",
     "en": "for “ab” (father) is put in the dual with respect to two different meanings, namely father and mother, and likewise “qamar” (moon) with respect to two different meanings, namely the moon and the sun?"},
    {"type": "matn",
     "ar": "قلنا: جاز أن يجعل الأم مسماة باسم الأب ادعاء لقوة التناسب بينهما، ثم يؤول",
     "en": "We say: the mother may be treated as named by the name of the father, by a claimed identification (iddiʿāʾ), owing to the strength of the affinity between them; then it is construed…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «عوض من لحوق … عوضا من لحوق» twice; the sense seems to call for a word like «عرض»/«عارض» or «حاصل»; transcribed as printed, translated as "arises from" (lit. "is a return (ʿiwaḍ) from").
    {"type": "pair",
     "ar": "وكذا صح أن الدلالة المذكورة عوض من لحوق الأمور الثلاثة باعتبار كونها عوضا من لحوق الأمرين بناء على لزوم الثالث لهما.",
     "en": "Likewise it is correct that the said indication arises from the attachment of the three things, in that it arises from the attachment of the two things, since the third necessarily accompanies them."},
    {"type": "pair",
     "ar": "والأظهر تأخير قوله: ونون مكسورة عن قوله: ليدل كما في اللباب.",
     "en": "It is more evident to place his words “and a nūn with kasra” after his words “so as to indicate”, as in al-Lubāb."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا يؤيد تقدير المفرد في التعريف.",
     "en": "This supports supposing “singular” in the definition."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حقيقيا أو اعتباريا، فإنه يجوز تثنية اسم الجمع، والجمع المكسر غير الأقصى على تأويل فرقتين كجمالين وقومين.",
     "en": "Real or by consideration; for the collective noun (ism al-jamʿ) and the broken plural other than the furthest plural may be put in the dual in the sense of two groups, like “jimālayn” and “qawmayn”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: ليس المراد من كونه من جنسه أن يكونا متفقين في الحقيقة، بل في الجنس الذي وضع ذلك المفرد له",
     "en": "He means: “its being of its genus” does not mean that the two agree in reality, but in the genus for which that singular was coined,"},
    {"type": "pair",
     "ar": "سواء اتفقا في الحقيقة كرجلين أو اختلفا نحو: أبيضين لإنسان وفرس.",
     "en": "whether they agree in reality, like “rajulayn” (two men), or differ, as in “abyaḍayn” (two white ones) for a man and a horse."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بالمعنى الأعم للوضع أعني: تعيين اللفظ للدلالة على معنى بنفسه، أو بقرينة، فيشمل المثنى المجازي أيضا كالأسدين.",
     "en": "In the wider sense of coinage (waḍʿ), namely assigning a word to indicate a meaning by itself or by a contextual indicator (qarīna); so it includes the figurative dual too, like “al-asadayn” (the two lions)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إشارة إلى أن اشتراك الجنس بينهما مفهوم من لفظ المثنى.",
     "en": "An indication that their sharing the genus is understood from the word of the dual."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وما وقع في تعريف الجمع المذكر السالم من قوله: ليدل على أن معه أكثر من جنسه يدل على أن المراد من قوله: مثله المثلية في الوحدة،",
     "en": "What occurs in the definition of the sound masculine plural, his words “so as to indicate that with it is more of its genus”, shows that what is meant by his words “its like” is likeness in unity,"},
    {"type": "pair",
     "ar": "ولا يدل على أن المراد المثلية في الجنس مع المثلية في الوحدة.",
     "en": "and does not show that what is meant is likeness in genus together with likeness in unity."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هذا كلام الهندي، وتبعه الشارح، وليس بذاك؛",
     "en": "This is the statement of al-Hindī, and the commentator followed him; but it is not sound,"},
    {"type": "pair",
     "ar": "لأن هذه الإرادة بعيدة بالنظر إلى ما ذكر في تعريف الجمع حيث قال: ليدل على أن معه أكثر منه من جنسه،",
     "en": "because this intended meaning is remote in view of what is said in the definition of the plural, where he said “so as to indicate that with it is more than it, of its genus”;"},
    {"type": "pair",
     "ar": "فإن الناظر فيه لا يفهم من قوله: مثله إلا ما يقابل الأكثر.",
     "en": "for one who considers it understands from his words “its like” only what stands opposite “more”."},
    {"type": "pair",
     "ar": "وبهذا ظهر ضعف احتمال المماثلة في اللفظ كما ذكره الهندي.",
     "en": "By this the weakness of the possibility of likeness in wording, as al-Hindī mentioned, becomes clear."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: أنه لا يجوز تثنية الاسم باعتبار معنيين مختلفين.",
     "en": "That is, that a noun may not be put in the dual with respect to two different meanings."},
]
